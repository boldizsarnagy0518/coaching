import csv
import io
from unittest.mock import patch, MagicMock
from django.test import SimpleTestCase, TestCase
from django.contrib.auth import get_user_model
from datetime import date
import uuid
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from .models import SetLog, TrainingPlan, Athlete, TrainingSession, PlannedSet
from .transfers import read_csv, safe_cell, published_sheet_url, download_sheet, GoogleRedirects, MAX_BYTES
from urllib.request import Request


class CsvTests(SimpleTestCase):
    def test_delimiters_bom_and_quoted_values(self):
        for data in ['\ufeffexercise,reps\r\n"Bench, paused",5', 'exercise;weight\nBench;60,5', 'exercise\treps\nBench\t5']:
            self.assertEqual(read_csv(data.encode('utf-8'))['row_count'], 1)

    def test_malformed_inputs(self):
        for data in [b'', b'<html>Login</html>', b'a,a\n1,2', b'a,\n1,2', b'a,b\n1,2\n3,4,5', b'\xff', b'x' * (MAX_BYTES + 1)]:
            with self.subTest(data=data[:30]), self.assertRaises(ValueError):
                read_csv(data)

    def test_preview_is_bounded(self):
        data = 'a,b\n' + '1,2\n' * 30
        self.assertEqual(len(read_csv(data.encode())['rows']), 20)
        self.assertEqual(read_csv(data.encode())['row_count'], 30)

    def test_formula_protection(self):
        for value in ['=1+1', '+cmd', '-1', '@x', '  =x', '\tfoo']:
            self.assertTrue(safe_cell(value).startswith("'"))
        self.assertEqual(safe_cell('Bench'), 'Bench')

    def test_google_url_restrictions(self):
        good = 'https://docs.google.com/spreadsheets/d/e/test_id/pub?output=csv&gid=0'
        self.assertIn('gid=0', published_sheet_url(good))
        for url in ['http://127.0.0.1/a', 'https://evil.example/a', good.replace('docs.google.com', 'docs.google.com.evil.example'), good.replace('output=csv', 'output=html')]:
            with self.subTest(url=url), self.assertRaises(ValueError):
                published_sheet_url(url)

    def test_unsafe_redirect_rejected(self):
        for url in ['http://docs.google.com/a', 'https://127.0.0.1/a', 'https://evil.example/a']:
            with self.assertRaises(ValueError):
                GoogleRedirects().redirect_request(Request('https://docs.google.com'), None, 302, '', {}, url)

    @patch('training.transfers.build_opener')
    def test_online_download_uses_same_reader(self, factory):
        response = MagicMock()
        response.read.return_value = b'exercise,reps\nBench,5'
        factory.return_value.open.return_value.__enter__.return_value = response
        self.assertEqual(download_sheet('https://docs.google.com/spreadsheets/d/e/test/pub?output=csv')['row_count'], 1)
        response.read.assert_called_once_with(MAX_BYTES + 1)


class TransferViewTests(TestCase):
    def setUp(self):
        self.coach = get_user_model().objects.create_user(username='coach')
        self.other = get_user_model().objects.create_user(username='other')
        self.athlete = Athlete.objects.create(coach=self.coach, name='Synthetic')
        plan = TrainingPlan.objects.create(athlete=self.athlete, title='Plan')
        session = TrainingSession.objects.create(plan=plan, title='Day', scheduled_date=date(2026, 10, 17))
        self.item = PlannedSet.objects.create(session=session, exercise='Bench', reps=5, weight_kg=100)
        self.client.force_login(self.coach)

    def test_export_contains_actual_and_planned(self):
        self.client.post(reverse('log-set', args=[self.item.pk]), {'submission_id': str(uuid.uuid4()), 'reps': 4, 'weight_kg': '97.5', 'rpe': '8'})
        response = self.client.get(reverse('export-csv', args=[self.athlete.pk]))
        rows = list(csv.DictReader(io.StringIO(response.content.decode('utf-8-sig'))))
        self.assertEqual(rows[0]['planned_reps'], '5')
        self.assertEqual(rows[0]['actual_reps'], '4')

    def test_foreign_transfer_access_blocked_before_fetch(self):
        self.client.force_login(self.other)
        with patch('training.views.download_sheet') as fetch:
            for name in ['export-csv', 'transfer-preview']:
                url = reverse(name, args=[self.athlete.pk])
                self.assertEqual(self.client.get(url).status_code, 404)
                self.assertEqual(self.client.post(url, {'sheet_url': 'https://example.com'}).status_code, 404)
            fetch.assert_not_called()

    def test_upload_is_preview_only(self):
        response = self.client.post(reverse('transfer-preview', args=[self.athlete.pk]), {
            'csv_file': SimpleUploadedFile('sheet.csv', b'exercise,reps\nBench,5')})
        self.assertEqual(response.context['preview']['row_count'], 1)
        self.assertFalse(SetLog.objects.exists())
        self.assertEqual(TrainingPlan.objects.count(), 1)

    def test_initial_get_shows_no_errors(self):
        response = self.client.get(reverse('transfer-preview', args=[self.athlete.pk]))
        self.assertFalse(response.context['form'].is_bound)
        self.assertNotContains(response, 'Vagy CSV-fájlt válassz')

    def test_source_choice_and_login(self):
        url = reverse('transfer-preview', args=[self.athlete.pk])
        self.assertTrue(self.client.post(url, {}).context['form'].errors)
        self.client.logout()
        self.assertEqual(self.client.get(url).status_code, 302)
        self.assertEqual(self.client.get(reverse('export-csv', args=[self.athlete.pk])).status_code, 302)

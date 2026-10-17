"""Request IDs, request timing, domain event logging and a health check.

Logs carry ids, statuses and durations only. Free text written by coaches or the AI
(names, memory content, reasons) must never be passed to ``log_event``.
"""
import contextvars
import logging
import re
import time
import uuid

from django.db import connection
from django.http import JsonResponse

request_id_var = contextvars.ContextVar("request_id", default="-")
SAFE_REQUEST_ID = re.compile(r"^[A-Za-z0-9_-]{8,64}$")
request_logger = logging.getLogger("coaching.request")
event_logger = logging.getLogger("coaching.events")


class RequestIdFilter(logging.Filter):
    """Adds ``request_id`` to every log record so one request's lines can be correlated."""

    def filter(self, record):
        record.request_id = request_id_var.get()
        return True


def _format(fields):
    return " ".join(f"{key}={value}" for key, value in fields.items())


def log_event(event, **fields):
    """Log a domain event as ``event=<name> key=value ...``; pass only ids, statuses and numbers."""
    event_logger.info(_format({"event": event, **fields}))


class RequestIdMiddleware:
    """Assigns a request ID (reusing a safe incoming X-Request-ID), times the request and logs one line."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        incoming = request.headers.get("X-Request-ID", "")
        request_id = incoming if SAFE_REQUEST_ID.match(incoming) else uuid.uuid4().hex
        token = request_id_var.set(request_id)
        started = time.perf_counter()
        status = 500
        try:
            response = self.get_response(request)
            status = response.status_code
            response["X-Request-ID"] = request_id
            return response
        finally:
            user = getattr(request, "user", None)
            level = logging.WARNING if status >= 500 else logging.INFO
            # The path is logged without the query string, which could contain user input.
            request_logger.log(level, _format({"method": request.method, "path": request.path, "status": status,
                "duration_ms": round((time.perf_counter() - started) * 1000, 1),
                "user": user.pk if user is not None and user.is_authenticated else "-"}))
            request_id_var.reset(token)


def healthz(request):
    """Liveness and database check for monitoring; reveals no data."""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
    except Exception:  # noqa: BLE001 - any database failure means unhealthy
        logging.getLogger("coaching.health").exception("health check failed")
        return JsonResponse({"status": "error", "database": "unavailable"}, status=503)
    return JsonResponse({"status": "ok", "database": "ok"})

from django.urls import path
from . import views

urlpatterns = [
    path("athletes/<int:pk>/export.csv", views.export_csv, name="export-csv"),
    path("athletes/<int:pk>/transfer/", views.transfer_preview, name="transfer-preview"),
    path("", views.dashboard, name="dashboard"),
    path("athletes/new/", views.athlete_create, name="athlete-create"),
    path("athletes/<int:pk>/", views.athlete_detail, name="athlete"),
    path("athletes/<int:pk>/plans/new/", views.plan_create, name="plan-create"),
    path("plans/<int:pk>/", views.plan_detail, name="plan"),
    path("plans/<int:pk>/sessions/new/", views.session_create, name="session-create"),
    path("sessions/<int:pk>/", views.session_detail, name="session"),
    path("sessions/<int:pk>/sets/new/", views.set_create, name="set-create"),
    path("sets/<int:pk>/log/", views.log_set, name="log-set"),
]

urlpatterns += [
    path("sessions/<int:pk>/change/<str:kind>/", views.session_change, name="session-change"),
    path("changes/<int:pk>/", views.change_detail, name="plan-change"),
    path("changes/<int:pk>/<str:action>/", views.change_review, name="plan-change-review"),
]

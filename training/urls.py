from django.urls import path
from . import views

urlpatterns = [
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

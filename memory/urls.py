from django.urls import path

from . import views

urlpatterns = [
    path("athletes/<int:pk>/memory/", views.athlete_memory, name="athlete-memory"),
    path("memory/<int:pk>/edit/", views.edit_memory, name="memory-edit"),
    path("memory/<int:pk>/<str:action>/", views.review_memory, name="memory-review"),
]

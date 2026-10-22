# tasks/urls.py
from django.urls import path
from . import views

app_name = "tasks"   # namespace de la app — ver nota más abajo

urlpatterns = [
    path("", views.home, name="home"),
    path("exposicionbdd/", views.exposicionbdd, name="expo")
]
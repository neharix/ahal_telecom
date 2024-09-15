from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.main),
    path("device/<int:device_pk>/", views.about_device),
]

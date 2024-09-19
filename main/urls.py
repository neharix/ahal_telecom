from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.main, name="home"),
    path("device/<int:device_pk>/", views.about_device),
    path("devices/<str:status>/", views.by_status),
    path("search-results/", views.search),
]

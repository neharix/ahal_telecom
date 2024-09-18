from django.urls import path

from .views import *

urlpatterns = [
    path("devices/<slug:slug>/", devices_api_view),
    path("devices/by_status/<str:status>/<slug:slug>/", devices_by_status_api_view),
]

from django.urls import path

from .views import *

urlpatterns = [path("devices/<slug:slug>/", devices_api_view)]

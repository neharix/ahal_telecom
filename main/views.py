from django.http import HttpRequest
from django.shortcuts import redirect, render

from .models import *


def main(request: HttpRequest):
    device_types = DeviceType.objects.all()
    return render(
        request,
        "views/main.html",
        {"device_types": device_types, "current_page": "main"},
    )


def about_device(request: HttpRequest, device_pk: int):
    device = Device.objects.get(pk=device_pk)
    return render(request, "views/about_device.html", {"device": device})

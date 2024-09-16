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
    if device.status == "ST":
        status = "Durnukly"
    elif device.status == "ER":
        status = "Näsazlyk"
    elif device.status == "FC":
        status = "Düzedilmez ýagdaýda"
    technical_works = TechnicalWork.objects.filter(device=device).order_by("-date_time")
    return render(
        request,
        "views/about_device.html",
        {"device": device, "status": status, "technical_works": technical_works},
    )

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import redirect, render

from .models import *


@login_required(login_url="/admin/login/")
def main(request: HttpRequest):
    device_types = DeviceType.objects.all()
    return render(
        request,
        "views/main.html",
        {"device_types": device_types, "current_page": "main"},
    )


@login_required(login_url="/admin/login/")
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


@login_required(login_url="/admin/login/")
def by_status(request: HttpRequest, status: str):
    device_types = DeviceType.objects.all()
    return render(
        request,
        "views/by_status.html",
        {"status": status, "device_types": device_types},
    )

from django.http import HttpRequest
from django.shortcuts import redirect, render

from .models import *


def main(request: HttpRequest):
    device_types = DeviceType.objects.all()
    return render(request, "views/main.html", {"device_types": device_types})

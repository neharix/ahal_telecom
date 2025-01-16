from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from UniWeb.models import *

from .models import Device


def home_view(request, *args, **kwargs):
    try:
        context = {"page_data": MainPageContent.objects.all()[0]}
    except:
        context = {}
    return render(request, "index.html", context)


def error404_view(request, *args, **kwargs):
    return render(request, "404.html", {})


def about_view(request, *args, **kwargs):
    try:
        context = {"page_data": AboutPage.objects.all()[0]}
    except:
        context = {}
    return render(request, "about.html", context)


def admissions_view(request, *args, **kwargs):
    try:
        context = {"page_data": AdmissionsPage.objects.all()[0]}
    except:
        context = {}
    device_type_names = [
        device_type.name for device_type in DeviceType.objects.all()[:3]
    ]
    students_count = [
        [
            device_type.first_year_production
            for device_type in DeviceType.objects.all()[:3]
        ]
    ]
    students_count.append(
        [
            device_type.second_year_production
            for device_type in DeviceType.objects.all()[:3]
        ]
    )
    students_count.append(
        [
            device_type.third_year_production
            for device_type in DeviceType.objects.all()[:3]
        ]
    )
    students_count.append(
        [
            device_type.fourth_year_production
            for device_type in DeviceType.objects.all()[:3]
        ]
    )
    students_count.append(
        [
            device_type.fifth_year_production
            for device_type in DeviceType.objects.all()[:3]
        ]
    )
    context["device_type_names"] = device_type_names
    context["students_count"] = students_count
    context["devices"] = Device.objects.all()
    return render(request, "admissions.html", context)


def about_device(request, device_id):
    return render(request, "device.html", {"device": Device.objects.get(id=device_id)})

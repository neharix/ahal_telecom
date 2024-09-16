from django.contrib import admin

from .models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["pk", "user", "specialization"]


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "image",
        "description",
        "status",
        "status_desc",
        "device_type",
    ]


@admin.register(DeviceType)
class DeviceTypeAdmin(admin.ModelAdmin):
    list_display = ["pk", "name"]


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ["pk", "value"]


@admin.register(TechnicalWork)
class TechnicalWorkAdmin(admin.ModelAdmin):
    list_display = ["worker", "date_time", "report", "device"]

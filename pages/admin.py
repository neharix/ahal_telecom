from django.contrib import admin

from .models import Device, DeviceType


# Register your models here.
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "d_type", "id")
    readonly_fields = ("id",)


@admin.register(DeviceType)
class DeviceTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "id")
    readonly_fields = ("id",)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.request import HttpRequest
from rest_framework.response import Response

from main.models import *

from .containers import *
from .serializers import *


@api_view(["GET"])
def devices_api_view(request: HttpRequest, slug: str):
    devices = Device.objects.filter(device_type__short=slug)
    devices_list = [DeviceContainer(device, slug) for device in devices]
    serializer = DeviceSerializer(devices_list, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def devices_by_status_api_view(request: HttpRequest, status: str, slug: str):
    devices = Device.objects.filter(device_type__short=slug, status=status)
    devices_list = [DeviceContainer(device, slug) for device in devices]
    serializer = DeviceSerializer(devices_list, many=True)
    return Response(serializer.data)

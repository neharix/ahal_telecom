from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.request import HttpRequest
from rest_framework.response import Response

from main.models import *

from .serializers import *


@api_view(["GET"])
def devices_api_view(request: HttpRequest, slug: str):
    devices = Device.objects.filter(device_type__short=slug)
    serializer = DeviceSerializer(devices, many=True)
    return Response(serializer.data)

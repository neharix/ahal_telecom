from rest_framework import serializers

from main.models import *


class DeviceSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    status = serializers.CharField()
    name = serializers.CharField()
    image = serializers.CharField()
    description = serializers.CharField()
    status_desc = serializers.CharField()
    device_type = serializers.CharField()
    device_type_slug = serializers.CharField()

from rest_framework import serializers

from main.models import *


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Device

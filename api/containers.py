from main.models import *


class DeviceContainer:
    def __init__(self, device: Device, slug: str) -> None:
        self.pk = device.pk
        if device.status == "ST":
            self.status = "Durnukly"
        elif device.status == "ER":
            self.status = "Näsazlyk"
        elif device.status == "FC":
            self.status = "Düzedilmez Ýagdaýda"
        self.name = device.name
        self.image = device.image
        self.description = device.description
        self.status_desc = device.status_desc
        self.device_type = device.device_type.name
        self.device_type_slug = slug

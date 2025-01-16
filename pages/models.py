from django.db import models


class DeviceType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Device(models.Model):
    class Status(models.TextChoices):
        STABLE = "DURNUKLY", "Durnukly"
        DISABLED = "IŞJEŇ DÄL ÝAGDAÝDA", "Işjeň däl ýagdaýda"
        OFFLINE = "ÖÇÜRILEN", "Öçürilen"

    name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to="devices/")
    status = models.CharField(max_length=20, choices=Status.choices)
    d_type = models.ForeignKey(
        "DeviceType", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.name

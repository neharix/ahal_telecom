from django.contrib.auth.models import User
from django.db import models


class StableManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(status=Device.Status.STABLE)


class ErrorManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(status=Device.Status.ERROR)


class FaultyManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(status=Device.Status.FAULTY_CONDITION)


class Device(models.Model):
    class Status(models.TextChoices):
        STABLE = "ST", "Durnukly"
        ERROR = "ER", "Näsazlyk"
        FAULTY_CONDITION = "FC", "Düzedilmez Ýagdaýda"

    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.STABLE
    )
    status_desc = models.TextField(null=True, blank=True)
    device_type = models.ForeignKey("DeviceType", on_delete=models.CASCADE)

    objects = models.Manager()
    stable = StableManager()
    error = ErrorManager()
    faulty = FaultyManager()

    def __str__(self):
        return self.name


class DeviceType(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.ForeignKey("Specialization", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Specialization(models.Model):
    value = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.value


class TechnicalWork(models.Model):
    worker = models.ForeignKey("Profile")
    report = models.TextField()
    device = models.ForeignKey("Device")

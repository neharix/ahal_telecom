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

    image = models.ImageField(verbose_name="Suraty", upload_to="devices/")
    name = models.CharField(verbose_name="Ady", max_length=250)
    description = models.TextField(verbose_name="Maglumat", null=True, blank=True)
    status = models.CharField(
        verbose_name="Ýagdaýy",
        max_length=2,
        choices=Status.choices,
        default=Status.STABLE,
    )
    status_desc = models.TextField(
        verbose_name="Ýagdaýy hakynda maglumat", null=True, blank=True
    )
    device_type = models.ForeignKey(
        "DeviceType", verbose_name="Enjam görnüşi", on_delete=models.CASCADE
    )

    objects = models.Manager()
    stable = StableManager()
    error = ErrorManager()
    faulty = FaultyManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "enjam"
        verbose_name_plural = "enjamlar"


class DeviceType(models.Model):
    name = models.CharField(verbose_name="Ady", max_length=250)
    short = models.SlugField(verbose_name="Gysgaltmasy", max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "enjam görnüşi"
        verbose_name_plural = "enjam görnüşleri"


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name="Ulanyjy", on_delete=models.CASCADE)
    specialization = models.ForeignKey(
        "Specialization", verbose_name="Hünäri", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "profil"
        verbose_name_plural = "profiller"


class Specialization(models.Model):
    value = models.CharField(verbose_name="Hünäri", max_length=250)

    def __str__(self) -> str:
        return self.value

    class Meta:
        verbose_name = "hünär"
        verbose_name_plural = "hünärler"


class TechnicalWork(models.Model):
    worker = models.ForeignKey(
        "Profile", verbose_name="Işgär", on_delete=models.PROTECT
    )
    date_time = models.DateTimeField(verbose_name="Wagty", auto_now_add=True)
    report = models.TextField(verbose_name="Raport")
    device = models.ForeignKey("Device", verbose_name="Enjam", on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.date_time.strftime("%d.%m.%Y %H:%M:%S")

    class Meta:
        verbose_name = "tehniki iş"
        verbose_name_plural = "tehniki işler"

from django.db import models


class DeviceType(models.Model):
    name = models.CharField(max_length=250)
    first_year_production = models.IntegerField()
    second_year_production = models.IntegerField()
    third_year_production = models.IntegerField()
    fourth_year_production = models.IntegerField()
    fifth_year_production = models.IntegerField()

    def __str__(self):
        return self.name


class CarouselImage(models.Model):
    header = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="carousel/")

    def __str__(self):
        return self.header


class InfoColumn(models.Model):
    expression = models.CharField(max_length=200)
    value = models.CharField(max_length=20)

    def __str__(self):
        return self.expression


class AboutInfoColumn(models.Model):
    expression = models.CharField(max_length=200)
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.expression


class MainPageContent(models.Model):
    main_heading = models.CharField(max_length=200)
    sub_heading = models.CharField(max_length=200)
    image = models.ImageField(upload_to="main_page/")
    info_columns = models.ManyToManyField(InfoColumn)
    about_heading = models.CharField(max_length=200)
    about_description = models.CharField(max_length=200)
    carousel_images = models.ManyToManyField(CarouselImage)

    def __str__(self):
        return f"{self.id}. Baş sahypa maglumatlary"


class AdmissionsPage(models.Model):
    header = models.CharField(max_length=200)
    content = models.CharField(max_length=750)
    muted_text = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.id}. Enjam üpjünçiligi sahypa maglumatlary"


class AboutPage(models.Model):
    main_heading = models.CharField(max_length=200)
    sub_heading = models.CharField(max_length=200)
    info_columns = models.ManyToManyField(AboutInfoColumn)

    def __str__(self):
        return f'{self.id}. "Biz barada" sahypa maglumatlary'

from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import *

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(MainPageContent)
admin.site.register(AdmissionsPage)
admin.site.register(AboutPage)
admin.site.register(InfoColumn)
admin.site.register(AboutInfoColumn)
admin.site.register(CarouselImage)


@admin.register(DeviceType)
class FacultyAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "first_year_production",
        "second_year_production",
        "third_year_production",
        "fourth_year_production",
        "fifth_year_production",
    ]

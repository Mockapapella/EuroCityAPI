from django.contrib import admin

# Register your models here.
from .models import Country


class CountryAdmin(admin.ModelAdmin):
    list_display = ("city_name", "country_name", "request_number")


admin.site.register(Country, CountryAdmin)

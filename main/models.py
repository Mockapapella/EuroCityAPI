from django.apps import AppConfig
from django.db import models


class Country(models.Model):

    city_name = models.CharField(max_length=200, default=None)
    country_name = models.CharField(max_length=200, default=None)
    request_number = models.IntegerField(default=1)

    class Meta:
        """Meta definition for Portfolio."""

        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        """Unicode representation of Portfolio."""
        return self.country_name

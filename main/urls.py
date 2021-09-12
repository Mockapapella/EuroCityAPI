from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path("country/<str:city_name>/", views.country_response),
]

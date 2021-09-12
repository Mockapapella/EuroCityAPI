import requests
from django.http import JsonResponse

from .models import Country


# Create your views here.
def country_response(request, city_name):
    try:
        country_object = Country.objects.filter(city_name__iexact=city_name)[0]
        country_object.request_number += 1
        country_object.save()
        country = {"country": country_object.country_name}
        return JsonResponse(country)
    except IndexError:
        country = requests.get(
            f"https://restcountries.eu/rest/v2/capital/{city_name}", params=request.GET
        )
        if country.status_code == 400:
            return JsonResponse(
                data={"status": 400, "message": "Bad request syntax or unsupported method"},
                status=400,
            )
        elif country.status_code == 404:
            return JsonResponse(
                data={"status": 404, "message": "No country found for given capital"}, status=404
            )
        elif country.status_code == 200:
            country = country.json()[0]
            if country["region"] != "Europe":
                return JsonResponse(
                    data={"status": 400, "message": "Country capital not located in Europe"},
                    status=400,
                )
            Country.objects.create(city_name=country["capital"], country_name=country["name"])
            return JsonResponse({"country": country["name"]})
        else:
            return JsonResponse(
                data={
                    "status": 404,
                    "message": "No resources were found that could satisfy your request",
                },
                status=404,
            )

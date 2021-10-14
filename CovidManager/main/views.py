from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpRequest, HttpResponseForbidden
import requests

import urllib.request, json
# Create your views here.

"countriys 800count"
"https://api.apify.com/v2/key-value-stores/tVaYRsPHLjNdNBu7S/records/LATEST?disableRedirect=true&desc=true"

"https://api.apify.com/v2/datasets/5JO5GL1h8Qv1CnG0m/items?format=json&limit=10&offset=0&desc=true"


def index(request: HttpRequest):
    with requests.get('https://disease.sh/v3/covid-19/historical/ru?lastdays=30') as url:
        data = url.json()
        cases = list(data["timeline"]["cases"].values())
        deaths = list(data["timeline"]["deaths"].values())
        recovered = list(data["timeline"]["recovered"].values())
        dates = list(data["timeline"]["cases"].keys())
        print(data)
        print(dates)
        print(cases)

        return render(request, 'main/InfoCountries.html', context={"cases": cases, "deaths": deaths, "recovered": recovered, "dates": dates})

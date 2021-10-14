from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpRequest, HttpResponseForbidden
import requests

import urllib.request, json
# Create your views here.

"countriys 800count"
"https://api.apify.com/v2/key-value-stores/tVaYRsPHLjNdNBu7S/records/LATEST?disableRedirect=true&desc=true"

"https://api.apify.com/v2/datasets/5JO5GL1h8Qv1CnG0m/items?format=json&limit=10&offset=0&desc=true"

month_list = ['янв', 'фев', 'мар', 'апр', 'мая', 'июн',
              'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
def index(request: HttpRequest):
    with requests.get('https://disease.sh/v3/covid-19/historical/ru?lastdays=all') as url:
        data = url.json()
        tl = data["timeline"]
        nn = 2
        cases = list(tl["cases"].values())
        cases = [cases[i] for i in range(len(cases)) if i % nn == 0]
        deaths = list(tl["deaths"].values())
        deaths = [deaths[i] for i in range(len(deaths)) if i % nn == 0]
        recovered = list(tl["recovered"].values())
        recovered = [recovered[i] for i in range(len(recovered)) if i % nn == 0]
        dates = list(tl["cases"].keys())
        dataf = lambda d: d[1]+" "+month_list[int(d[0]) - 1] + " " + d[2]+"г."
        dates = [dataf(dates[i].split("/")) for i in range(len(dates)) if i % nn == 0]

        print(data)
        print(dates)
        print(cases)

        return render(request, 'main/InfoRussian.html', context={"cases": cases, "deaths": deaths,
                                                                   "recovered": recovered, "dates": dates})

# from django.shortcuts import render
from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect, Http404, HttpRequest, HttpResponseForbidden
import requests
from .regions import *
date_update = dates[-1]

import urllib.request, json

# Create your views here.

"countriys 800count"
"https://api.apify.com/v2/key-value-stores/tVaYRsPHLjNdNBu7S/records/LATEST?disableRedirect=true&desc=true"

"https://api.apify.com/v2/datasets/5JO5GL1h8Qv1CnG0m/items?format=json&limit=10&offset=0&desc=true"

month_list = ['янв', 'фев', 'мар', 'апр', 'мая', 'июн',
              'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']

urls_api_ru = (
    'https://disease.sh/v3/covid-19/historical/ru?lastdays=all',
    'https://disease.sh/v3/covid-19/countries/ru?strict=true',
    "https://disease.sh/v3/covid-19/vaccine/coverage/countries/ru?lastdays=all&fullData=false"
)


def statistic_ru(request: HttpRequest):
    region = "Россия"
    if request.method == 'GET':
        region = request.GET.get('region', region)
    elif request.method == "POST":
        region = request.POST.get('region', region)
    reg_id = regions_id[region]
    if reg_id == "255":
        context = statistic_context(request, urls_api_ru)
    else:
        context = statistic_region_context(reg_id)

    datef = lambda d: d[1] + " " + month_list[int(d[0]) - 1] + "20 " + d[2] + "г."
    context["regions_title"] = regions_title
    context["regions"] = regions
    context["country_title"] = region
    context["regions_list"] = regions_title
    context["date_update"] = datef(context["dates_list"][-1])
    
    context["date_update"] = date_update
    print("context", context)
    
    return render(request, "main/RussianMap.html", context=context)


def statistic_context(request: HttpRequest, urls_api: tuple):
    nn = 2
    # historycal
    with requests.get(urls_api[0]) as res_:
        print(res_)
        res = res_
        if res.status_code == 200:
            data = res.json()
            if "timeline" in data:
                tl = data["timeline"]
            else:
                tl = data
            count = len(tl.get("cases")) // nn
            cases = list(tl["cases"].values())
            cases_list = [cases[i] for i in range(len(cases)) if i % nn == 0]
            deaths = list(tl["deaths"].values())
            deaths_list = [deaths[i] for i in range(len(deaths)) if i % nn == 0]
            recovered = list(tl["recovered"].values())
            recovered_list = [recovered[i] for i in range(len(recovered)) if i % nn == 0]
            dates = list(tl["cases"].keys())
            dataf = lambda d: d[1] + " " + month_list[int(d[0]) - 1] + " " + d[2] + "г."
            dates_list = [dataf(dates[i].split("/")) for i in range(len(dates)) if i % nn == 0]
            
            print(data)
        else:
            count = 0
            cases_list = deaths_list = recovered_list = dates_list = 0
    
    # strings statistic
    with requests.get(urls_api[1]) as res:
        if res.status_code == 200:
            data = res.json()
            numf = lambda x: '{0:,}'.format(x).replace(',', ' ')
            cases = numf(data["cases"])
            todayCases = numf(data["todayCases"])
            deaths = numf(data["deaths"])
            recovered = numf(data["recovered"])
            tests = ">{},{} млн".format(data["tests"] // 1000000, data["tests"] % 1000000 // 100000)
        else:
            cases = 0
            todayCases = 0
            deaths = 0
            recovered = 0
            tests = 0
    
    # vaccine
    with requests.get(urls_api[2]) as res:
        if res.status_code == 200:
            data = res.json()
            if "timeline" in data:
                tl = data["timeline"]
            else:
                tl = data
            count2 = len(tl) // nn
            tests_list = list(tl.values())
            tests_list = [tests_list[i] for i in range(len(tests_list)) if i % nn == 0]
            tests_list = [0] * (count - count2) + tests_list
        else:
            count2 = 0
            tests_list = []
    print(len(tests_list), count2, count)
    
    return {"cases_list": cases_list, "deaths_list": deaths_list,
            "recovered_list": recovered_list, "dates_list": dates_list,
            "cases": cases, "deaths": deaths,
            "recovered": recovered, "tests_list": tests_list,
            "tests": tests, "todayCases": todayCases,
            }


def statistic_region_context(rid):
    nn = 2
    # historycal
    url = f"https://milab.s3.yandex.net/2020/covid19-stat/data/v10/data-by-region/{rid}.json"
    with requests.get(url) as res:
        # print(res)
        if res.status_code == 200:
            data = res.json()
            count = len(data.get("cases")) // nn
            cases = data["cases"]
            cases_list = [cases[i][0] for i in range(len(cases)) if i % nn == 0]
            cases_delta_list = [cases[i][1] for i in range(len(cases)) if i % nn == 0]
            deaths = data["deaths"]
            deaths_list = [deaths[i][0] for i in range(len(deaths)) if i % nn == 0]
            deaths_delta_list = [deaths[i][1] for i in range(len(deaths)) if i % nn == 0]
            recovered_list = []
            
            dataf = lambda d: d[2] + " " + month_list[int(d[1]) - 1] + " " + d[0] + "г."
            dates_list = [dataf(dates[i].split("-")) for i in range(len(dates)) if i % nn == 0]
            
            numf = lambda x: '{0:,}'.format(x).replace(',', ' ')
            info = data["info"]
            cases = (info["cases"])
            todayCases = (info["cases_delta"])
            todayDeaths = (info["deaths_delta"])
            deaths = (info["deaths"])
            
            cases_b = numf(info["cases"])
            todayCases_b = numf(info["cases_delta"])
            todayDeaths_b = numf(info["deaths_delta"])
            deaths_b = numf(info["deaths"])
            recovered = -1
            tests = -1
            
            tests_list = []
            # print(data)
        else:
            count = 0
            cases_list = deaths_list = recovered_list = dates_list = []
            tests_list = []
            
            cases = 0
            todayCases = 0
            todayDeaths = 0
            deaths = 0
            recovered = 0
            tests = 0
    
    return {"cases_list": cases_list, "deaths_list": deaths_list,
            "recovered_list": recovered_list, "dates_list": dates_list,
            "cases": cases, "todayCases": todayCases,
            "deaths": deaths, "todayDeaths": todayDeaths,
            "cases_b": cases, "todayCases_b": todayCases,
            "deaths_b": deaths, "todayDeaths_b": todayDeaths,
            "recovered": recovered, "tests_list": tests_list,
            "tests": tests,
            "cases_delta_list": cases_delta_list,
            "deaths_delta_list": deaths_delta_list,
            "regions_top_title": regions_top_title,
            "regions_top_cases": regions_top_cases,
            "regions_top_deaths": regions_top_deaths
            }


def statistic_ru_old(request: HttpRequest):
    urls_api = (
        'https://disease.sh/v3/covid-19/historical/ru?lastdays=all',
        'https://disease.sh/v3/covid-19/countries/ru?strict=true',
        "https://disease.sh/v3/covid-19/vaccine/coverage/countries/ru?lastdays=all&fullData=false"
    )
    
    if request.method == 'GET':
        region = request.GET.get('region', None)
        reg_id = regions_id[region]
        if reg_id == "255":
            region = None
    elif request.method == "POST":
        region = request.POST['region']
        reg_id = regions_id[region]
        if reg_id == "255":
            region = None
    else:
        region = None
    if region:
        context = statistic_region_context(reg_id)
    else:
        context = statistic_context(request, urls_api)
        region = "Россия"
        context["region"] = "Россия"
    
    context["region"] = context["country_title"] = region
    context["regions_list"] = regions_title
    print("regions:", regions_title)
    return render(request, 'main/InfoRussian.html', context=context)


def statistic_world(request: HttpRequest, country=None):
    urls_api = (
        'https://disease.sh/v3/covid-19/historical/all?lastdays=all',
        'https://disease.sh/v3/covid-19/all?strict=true',
        "https://disease.sh/v3/covid-19/vaccine/coverage/?lastdays=all&fullData=false"
    )
    if request.method == 'GET':
        country = request.GET.get('country', None)
    elif request.method == "POST":
        country = request.POST['country']
    else:
        country = None
    if country == "Russia":
        return redirect("main:ru")
    if country and country != "World":
        urls_api = (
            f'https://disease.sh/v3/covid-19/historical/{country}?lastdays=all',
            f'https://disease.sh/v3/covid-19/countries/{country}?strict=true',
            f"https://disease.sh/v3/covid-19/vaccine/coverage/countries/{country}?lastdays=all&fullData=false"
        )
        print(urls_api)
    context = statistic_context(request, urls_api)
    context["country_title"] = country or "Мир"
    context["countries_list"] = ["World"] + get_countries_list()
    
    return render(request, 'main/InfoWorld.html', context=context)


def get_countries_list():
    url = "https://disease.sh/v3/covid-19/continents"
    with requests.get(url) as req:
        data = req.json()
        lst = [ctr for contin in data for ctr in contin["countries"] if " " not in ctr]
        print(lst)
    return lst

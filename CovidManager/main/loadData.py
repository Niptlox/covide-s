import requests
import json

month_list = ['янв', 'фев', 'мар', 'апр', 'мая', 'июн',
              'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']

urls_api_all = (
    'https://disease.sh/v3/covid-19/historical/all?lastdays=all',
    'https://disease.sh/v3/covid-19/all?strict=true',
    "https://disease.sh/v3/covid-19/vaccine/coverage/?lastdays=all&fullData=false"
)
urls_api_ru = (
    'https://disease.sh/v3/covid-19/historical/ru?lastdays=all',
    'https://disease.sh/v3/covid-19/countries/ru?strict=true',
    "https://disease.sh/v3/covid-19/vaccine/coverage/countries/ru?lastdays=all&fullData=false"
)


def preparation_regions():
    regions_title = []
    with open('static/json/Russian.json', "r", encoding="utf-8") as f:
        print("preparation_regions")
        d = json.load(f)["russia_stat_struct"]
        dates = d["dates"]
        regions_id = {}
        regions = []
        cases = {}
        for rid, inf in d["data"].items():
            inf = inf["info"]
            name = inf["name"]
            regions_id[name] = rid
            regions_title.append(name)
            regions.append([name, inf["cases"], inf["cases_delta"], inf["deaths"], inf["deaths_delta"]])
    regions_title.sort()
    regions.sort(key=lambda x: x[0])
    regions_top = sorted(regions, key=lambda x: x[0] != "Россия" and x[1], reverse=True)[:10]
    regions_top_title, regions_top_cases, regions_top_deaths = [[item[i] for item in regions_top] for i in (0, 1, 3)]
    # print(regions_top_title, regions_top_cases, regions_top_deaths)
    return regions_id, regions_title, dates, regions, regions_top_title, regions_top_cases, regions_top_deaths


def reload_regions():
    url = "https://milab.s3.yandex.net/2020/covid19-stat/data/v10/default_data.json"
    with requests.get(url) as res_:
        print("reload_regions:", res_)
        res = res_
        if res.status_code == 200:
            data = res.json()
            with open('static/json/Russian.json', 'w') as f:
                json.dump(data, f)
        # print(data)


def reload_countries():
    url = "https://disease.sh/v3/covid-19/countries?yesterday=all&sort=cases"
    with requests.get(url) as res_:
        print("reload_countries:", res_)
        res = res_
        if res.status_code == 200:
            data = res.json()
            with open('static/json/Countries.json', 'w') as f:
                json.dump(data, f)
        # print(data)


def preparation_countries():
    with open('static/json/Countries.json', "r", encoding="utf-8") as f:
        print("preparation_countries")
        data = json.load(f)
        ctr_top = [[item[i] for item in data[:5]] for i in
                   ("country", "cases", "deaths", "recovered")]
        
        return ctr_top


def get_countries_list():
    url = "https://disease.sh/v3/covid-19/continents"
    with requests.get(url) as req:
        print("countries_list:", req)
        data = req.json()
        lst = [ctr for contin in data for ctr in contin["countries"] if " " not in ctr]
        # print(lst)
    return lst


def statistic_context(urls_api: tuple):
    nn = 2
    # historycal
    with requests.get(urls_api[0]) as res_:
        # print(res_)
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
            
            # print(data)
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


reload_countries()
reload_regions()

regions_id, regions_title, dates, regions, regions_top_title, regions_top_cases, regions_top_deaths = preparation_regions()
ctr_top = preparation_countries()

countries_list = get_countries_list()

context_all = statistic_context(urls_api_all)
context_ru = statistic_context(urls_api_ru)

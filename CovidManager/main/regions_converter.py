def load_regions():
    import json
    regions_title = []
    with open('../static/json/Russian.json', "r", encoding="utf-8") as f:
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
    return regions_id, regions_title, dates, regions


regions_id, regions_title, dates, regions = load_regions()

reg_ = [["RU-MOW", "Москва", "moscow.gif"],
        ["RU-CHE", "Челябинская область", "chelyabinskaya_flag.png"],
        ["RU-ORL", "Орловская область"],
        ["RU-OMS", "Омская область", "flag_omskoj_oblasti.png"],
        ["RU-LIP", "Липецкая область", "lipeckya.jpg"],
        ["RU-KRS", "Курская область", "flag_of_kursk_oblast.png"],
        ["RU-RYA", "Рязанская область", "ryazan.png"],
        ["RU-BRY", "Брянская область", "bryanskaya_flag.png"],
        ["RU-KIR", "Кировская область", "flag_kirovskoy_oblasti.png"],
        ["RU-ARK", "Архангельская область", ""],
        ["RU-MUR", "Мурманская область", ""],
        ["RU-SPE", "Санкт-Петербург", ""],
        ["RU-YAR", "Ярославская область", ""],
        ["RU-ULY", "Ульяновская область", ""],
        ["RU-NVS", "Новосибирская область", ""],
        ["RU-TYU", "Тюменская область", ""],
        ["RU-SVE", "Свердловская область", ""],
        ["RU-NGR", "Новгородская область", ""],
        ["RU-KGN", "Курганская область", ""],
        ["RU-KGD", "Калининградская область", ""],
        ["RU-IVA", "Ивановская область", ""],
        ["RU-AST", "Астраханская область", ""],
        ["RU-KHA", "Хабаровский край", ""],
        ["RU-CE", "Чеченская республика", ""],
        ["RU-UD", "Удмуртская республика", ""],
        ["RU-SE", "Республика Северная Осетия", ""],
        ["RU-MO", "Республика Мордовия", ""],
        ["RU-KR", "Республика  Карелия", ""],
        ["RU-KL", "Республика  Калмыкия", ""],
        ["RU-IN", "Республика  Ингушетия", ""],
        ["RU-AL", "Республика Алтай", ""],
        ["RU-BA", "Республика Башкортостан", ""],
        ["RU-AD", "Республика Адыгея", ""],
        ["RU-CR", "Республика Крым", ""],
        ["RU-SEV", "Севастополь", ""],
        ["RU-KO", "Республика Коми", ""],
        ["RU-PNZ", "Пензенская область", ""],
        ["RU-TAM", "Тамбовская область", ""],
        ["RU-LEN", "Ленинградская область", ""],
        ["RU-VLG", "Вологодская область", ""],
        ["RU-KOS", "Костромская область", ""],
        ["RU-PSK", "Псковская область", ""],
        ["RU-YAN", "Ямало-Ненецкий АО", ""],
        ["RU-CHU", "Чукотский АО", ""],
        ["RU-YEV", "Еврейская автономская область", ""],
        ["RU-TY", "Республика Тыва", ""],
        ["RU-SAK", "Сахалинская область", ""],
        ["RU-AMU", "Амурская область", ""],
        ["RU-BU", "Республика Бурятия", ""],
        ["RU-KK", "Республика Хакасия", ""],
        ["RU-KEM", "Кемеровская область", ""],
        ["RU-ALT", "Алтайский край", ""],
        ["RU-DA", "Республика Дагестан", ""],
        ["RU-KB", "Кабардино-Балкарская республика", ""],
        ["RU-KC", "Карачаевая-Черкесская республика", ""],
        ["RU-KDA", "Краснодарский край", ""],
        ["RU-ROS", "Ростовская область", ""],
        ["RU-SAM", "Самарская область", ""],
        ["RU-TA", "Республика Татарстан", ""],
        ["RU-ME", "Республика Марий Эл", ""],
        ["RU-CU", "Чувашская республика", ""],
        ["RU-NIZ", "Нижегородская край", ""],
        ["RU-VLA", "Владимировская область", ""],
        ["RU-MOS", "Московская область", ""],
        ["RU-KLU", "Калужская область", ""],
        ["RU-BEL", "Белгородская область", ""],
        ["RU-ZAB", "Забайкальский край", ""],
        ["RU-PRI", "Приморский край", ""],
        ["RU-KAM", "Камачатский край", ""],
        ["RU-MAG", "Магаданская область", ""],
        ["RU-SA", "Республика Саха", ""],
        ["RU-KYA", "Красноярский край", ""],
        ["RU-ORE", "Оренбургская область", ""],
        ["RU-SAR", "Саратовская область", ""],
        ["RU-VGG", "Волгоградская область", ""],
        ["RU-VOR", "Ставропольский край", ""],
        ["RU-SMO", "Смоленская область", ""],
        ["RU-TVE", "Тверская область", ""],
        ["RU-PER", "Пермская область", ""],
        ["RU-KHM", "Ханты-Мансийский АО", ""],
        ["RU-KHM", "Ханты-Мансийский АО", ""],
        ["RU-TOM", "Томская область", ""],
        ["RU-IRK", "Иркутская область", ""],
        ["RU-NEN", "Ненецскй АО", ""],
        ["RU-STA", "Ставропольский край", ""],
        ["RU-TUL", "Тульская область", "tulskaya_flag.png"]]

dict_r = {'Республика Северная Осетия': 'Республика Северная Осетия — Алания',
          'Карачаевая-Черкесская Республика': 'Карачаево-Черкесская Республика',
          'Нижегородская край': 'Нижегородская область', 'Владимировская область': 'Владимирская область',
          'Камачатский край': 'Камчатский край', 'Республика Саха': 'Республика Саха (Якутия)',
          'Пермская область': 'Пермский край',
          'Ханты-Мансийский автономный округ': 'Ханты-Мансийский автономный округ — Югра',
          'Ненецскй автономный округ': 'Ямало-Ненецкий автономный округ'}
for i in range(len(reg_)):
    r = reg_[i][1]
    r = r.replace("  ", " ")
    r = r.replace("АО", "автономный округ")
    r = r.replace("автономская", "автономная")
    r = r.replace("республика", "Республика")
    r = dict_r.get(r, r)
    reg_[i][1] = r

print(reg_)

ar1 = []
ar2 = []
for r in reg_:
    if len(r) == 2:
        r.append("")
    r += [regions_id[r[1]], str(regions_title.index(r[1]))]
    r = r[1]
    if r in regions_title:
        ar1.append(r)
    else:
        ar2.append(r)
print(ar1)
print(ar2)
print(reg_)

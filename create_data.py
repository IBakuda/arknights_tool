import requests
from bs4 import BeautifulSoup
import json
from find_url import generator_for_episodes, generator_side_stori_episodes, generator_intermezi

total_orundum = 0


def create_data():
    total_data = {'Episodes': {}, 'Side_story': {}, 'Intermezzi': {}}

    for iteration in generator_for_episodes():
        url = f'https://arknights.wiki.gg/wiki/{iteration}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find('table', class_="mrfz-wtable")
        try:
            o = data.find_all('span')[-1].text
        except:
            continue
        key = iteration.split('/')[-1]
        total_data['Episodes'][key] = {'total': int(o),
                                       'normal': 0,
                                       'chelenge': 0,
                                       'ex': 0,
                                       'clear': False}

    for iteration in generator_side_stori_episodes():
        url = f'https://arknights.wiki.gg{iteration}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        table = soup.find('table', class_="mrfz-wtable")
        try:
            o = table.find_all('span')[-1].text
        except:
            continue

        if int(o) > 100:
            alt_tables = soup.find_all('table', class_="mrfz-wtable")  # Получаем все таблицы
            for alt_table in alt_tables:
                if alt_table != table:  # Пропускаем уже проверенную
                    try:
                        o_alt = int(alt_table.find_all('span')[-1].text)
                        if o_alt <= 100:
                            o = o_alt
                            break
                    except:
                        continue  # Если не удается извлечь число, пробуем следующую таблицу
        key = iteration.split('/')[-1]
        total_data['Side_story'][key] = {'total': int(o),
                                         'normal': 0,
                                         'chelenge': 0,
                                         'ex': 0,
                                         'clear': False}

    for iteration in generator_intermezi():
        url = f'https://arknights.wiki.gg{iteration}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        table = soup.find('table', class_="mrfz-wtable")
        try:
            o = table.find_all('span')[-1].text
        except:
            continue
        key = iteration.split('/')[-1]
        total_data['Intermezzi'][key] = {'total': int(o),
                                         'normal': 0,
                                         'chelenge': 0,
                                         'ex': 0,
                                         'clear': False}

    # Записываем в файл "data.json"
    with open("data/data.json", "w", encoding="utf-8") as file:
        json.dump(total_data, file, indent=4, ensure_ascii=False)


def update_data():
    with open("data/data.json", "r", encoding="utf-8") as file:
        total_data = json.load(file)

    for iteration in generator_for_episodes():
        key = iteration.split('/')[-1]
        if key in total_data['Episodes']:
            continue
        else:

            url = f'https://arknights.wiki.gg/wiki/{iteration}'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "lxml")
            data = soup.find('table', class_="mrfz-wtable")
            try:
                o = data.find_all('span')[-1].text
            except:
                continue
            key = iteration.split('/')[-1]
            total_data['Episodes'][key] = {'total': int(o),
                                           'normal': 0,
                                           'chelenge': 0,
                                           'ex': 0,
                                           'clear': False}

    for iteration in generator_side_stori_episodes():
        key = iteration.split('/')[-1]
        if key in total_data['Side_story']:
            continue
        else:
            url = f'https://arknights.wiki.gg{iteration}'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "lxml")
            table = soup.find('table', class_="mrfz-wtable")
            try:
                o = table.find_all('span')[-1].text
            except:
                continue

            if int(o) > 100:
                alt_tables = soup.find_all('table', class_="mrfz-wtable")  # Получаем все таблицы
                for alt_table in alt_tables:
                    if alt_table != table:  # Пропускаем уже проверенную
                        try:
                            o_alt = int(alt_table.find_all('span')[-1].text)
                            if o_alt <= 100:
                                o = o_alt
                                break
                        except:
                            continue  # Если не удается извлечь число, пробуем следующую таблицу
            key = iteration.split('/')[-1]
            total_data['Side_story'][key] = {'total': int(o),
                                             'normal': 0,
                                             'chelenge': 0,
                                             'ex': 0,
                                             'clear': False}

    for iteration in generator_intermezi():
        key = iteration.split('/')[-1]
        if key in total_data['Intermezzi']:
            continue
        else:
            url = f'https://arknights.wiki.gg{iteration}'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "lxml")
            table = soup.find('table', class_="mrfz-wtable")
            try:
                o = table.find_all('span')[-1].text
            except:
                continue
            key = iteration.split('/')[-1]
            total_data['Intermezzi'][key] = {'total': int(o),
                                             'normal': 0,
                                             'chelenge': 0,
                                             'ex': 0,
                                             'clear': False}

    # Записываем в файл "data.json"
    with open("data/data.json", "w", encoding="utf-8") as file:
        json.dump(total_data, file, indent=4, ensure_ascii=False)


update_data()
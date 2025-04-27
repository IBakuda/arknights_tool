from django.db import connection

from ..models import StoryCost
import requests
from bs4 import BeautifulSoup
import json
from .find_url import generator_for_episodes, generator_side_stori_episodes, generator_intermezi


def create():
    delete_all()

    for enum, iteration in enumerate(generator_for_episodes()):
        url = f'https://arknights.wiki.gg/wiki/{iteration}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find('table', class_="mrfz-wtable")
        try:
            o = data.find_all('span')[-1].text
        except:
            continue
        key = iteration.split('/')[-1]
        db_action = StoryCost.objects.create(
            story_type='Main_theme',
            name=key,
            total=int(o),
            normal=0,
            challenge=0,
            extra=enum + 1,
        )
        db_action.save()

    for enum, iteration in enumerate(generator_side_stori_episodes()):
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
        db_action = StoryCost.objects.create(
            story_type='Side_story',
            name=key,
            total=int(o),
            normal=0,
            challenge=0,
            extra=enum + 1,
        )
        db_action.save()

    for enum, iteration in enumerate(generator_intermezi()):
        url = f'https://arknights.wiki.gg{iteration}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        table = soup.find('table', class_="mrfz-wtable")
        try:
            o = table.find_all('span')[-1].text
        except:
            continue
        key = iteration.split('/')[-1]
        db_action = StoryCost.objects.create(
            story_type='Intermezzi',
            name=key,
            total=int(o),
            normal=0,
            challenge=0,
            extra=enum + 1,
        )
        db_action.save()


def update():

    main_theme = StoryCost.objects.filter(story_type='Main_theme').values_list('name', flat=True)
    for enum, iteration in enumerate(generator_for_episodes()):
        key = iteration.split('/')[-1]
        if key in main_theme:
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
            db_action = StoryCost.objects.create(
                story_type='Main_theme',
                name=key,
                total=int(o),
                normal=0,
                challenge=0,
                extra=enum + 1,
            )
            db_action.save()

    side_stori = StoryCost.objects.filter(story_type='Side_story').values_list('name', flat=True)
    for enum, iteration in enumerate(generator_side_stori_episodes()):
        key = iteration.split('/')[-1]
        if key in side_stori:
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
            db_action = StoryCost.objects.create(
                story_type='Side_story',
                name=key,
                total=int(o),
                normal=0,
                challenge=0,
                extra=enum + 1,
            )
            db_action.save()

    intermezzi = StoryCost.objects.filter(story_type='Intermezzi').values_list('name', flat=True)
    for enum, iteration in enumerate(generator_intermezi()):
        key = iteration.split('/')[-1]
        if key in intermezzi:
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
            db_action = StoryCost.objects.create(
                story_type='Intermezzi',
                name=key,
                total=int(o),
                normal=0,
                challenge=0,
                extra=enum + 1,
            )
            db_action.save()


def delete_all():

    with connection.cursor() as cursor:
        cursor.execute("TRUNCATE TABLE main_storycost RESTART IDENTITY CASCADE;")


def delete():
    mass = ['Episode_12', 'Episode_13', 'Episode_14', 'Episode_11', 'Episode_10', 'Episode_09']
    val = StoryCost.objects.filter(story_type='Main_theme').values_list('name', flat=True)
    for i in mass:
        if i in val:
            item = StoryCost.objects.get(name=i)
            item.delete()
        else:
            continue

    mass = ['Lingering_Echoes', 'Mansfield_Break', 'Guide_Ahead', 'Where_Vernal_Winds_Will_Never_Blow', 'The_Rides_to_Lake_Silberneherze', 'Delicious_On_Terra']
    val = StoryCost.objects.filter(story_type='Side_story').values_list('name', flat=True)
    for i in mass:
        if i in val:
            item = StoryCost.objects.get(name=i)
            item.delete()
        else:
            continue

    mass = ['Babel_(event)', 'Darknights_Memoir', 'Stultifera_Navis']
    val = StoryCost.objects.filter(story_type='Intermezzi').values_list('name', flat=True)
    for i in mass:
        if i in val:
            item = StoryCost.objects.get(name=i)
            item.delete()
        else:
            continue


def chapter_clear(data):
    data = data
    for value in data:
        # id = value.id
        # total = value.total
        # normal = value.normal
        # challenge = value.challenge
        # clear = value.clear
        if value.clear:
            value.challenge = 8
            value.normal = value.total - value.challenge

        if value.challenge + value.normal == value.total:
            value.clear = True
        else:
            value.clear = False
        value.save()
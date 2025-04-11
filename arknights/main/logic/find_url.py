import re
import requests
from bs4 import BeautifulSoup


def generator_for_episodes():
    url_for_main = 'https://arknights.wiki.gg/wiki/Story'
    responce = requests.get(url_for_main)
    soup = BeautifulSoup(responce.text, 'lxml')
    data = soup.find('table', id='story-info-table')
    episode = data.find_all('a')
    for item in episode:
        res = item.get('href').split('/')[-1]
        if re.fullmatch(r'Episode_\d{2}', res) or res == 'Prologue':
            yield res


def generator_side_stori_episodes():
    url_for_main = 'https://arknights.wiki.gg/wiki/Story'
    responce = requests.get(url_for_main)
    soup = BeautifulSoup(responce.text, 'lxml')
    data = soup.find('article', id='Side_Stories-0')
    divs = [div for div in data.find_all('div') if not div.has_attr('class') and div.find('a')]

    for div in divs:
        try:
            yield div.find('a').get('href')
        except:
            break


def generator_intermezi():
    url_for_main = 'https://arknights.wiki.gg/wiki/Story'
    responce = requests.get(url_for_main)
    soup = BeautifulSoup(responce.text, 'lxml')
    data = soup.find('article', id='Intermezzi-0')
    divs = [div for div in data.find_all('div') if not div.has_attr('class') and div.find('a')]
    for div in divs:
        try:
            yield div.find('a').get('href')
        except:
            break















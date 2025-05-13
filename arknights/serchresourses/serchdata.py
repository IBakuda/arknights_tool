import requests
from bs4 import BeautifulSoup


def serchoperator(name):
    url = f'https://arknights.wiki.gg/wiki/{name}'
    responce = requests.get(url)
    soup = BeautifulSoup(responce.content, 'lxml')

    promotion = soup.find('table', id='operator-promotion-table')
    skils = soup.find('div', class_='mw-collapsible-content') # Попробуем найти <td> если не получится <tr>
    modeules = soup.find('table', class_='mrfz-wtable operator-module-prereq')

    # promotion_resourses = promotion.find_all('td')

    promotion_resources = []
    for td in promotion.find_all('td'):
        quantity_div = td.find('div', class_='quantity')
        item_img = td.find('img')
        if quantity_div or item_img:
            promotion_resources.append({
                'item': item_img.get('alt', 'Неизвестно'),
                'quantity': quantity_div.text.strip()
            })


    data ={
        'promotion_resourses': 1
    }

    return [promotion_resources]

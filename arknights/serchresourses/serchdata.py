import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def collect_data(resorse, en, w):
    BASE_URL = 'https://arknights.wiki.gg/'
    output = {}

    for i, td in enumerate(resorse, start=en):
        for div in td.find_all('div', recursive=w):

            item = div.find('div', class_='item-tooltip')
            quantity_div = div.find('div', class_='quantity')



            if quantity_div and item:

                item_found = item.get('data-name', 'Неизвестно')
                quantity_found = quantity_div.text.strip()
                img_tag = div.find('img', {'alt': lambda x: x and f'{item_found}.png' in x})
                full_img_url = ''

                if img_tag:
                    relative_src = img_tag['src']
                    full_img_url = urljoin(BASE_URL, relative_src)

                if i not in output:
                    output[i] = {}

                    # Добавляем item: quantity
                output[i][item_found] = [quantity_found, full_img_url]
    return output


def serchoperator(name):
    url = f'https://arknights.wiki.gg/wiki/{name}'
    responce = requests.get(url)
    soup = BeautifulSoup(responce.content, 'lxml')

    promotion = soup.find('table', id='operator-promotion-table')
    skils = soup.find('div', class_='mw-collapsible-content')
    modeules = soup.find_all('table', class_='mrfz-wtable operator-module-prereq')

    promotion_tds = promotion.find_all('td')
    promotion_resources = collect_data(promotion_tds, 1, True)

    skills_tds = skils.find_all('td')
    skils_resourses = collect_data(skills_tds, 2, True)


    modeules_resourses = {}
    for enum, item in enumerate(modeules, start=1):
        module_tds = item.find_all('td')
        modeules_resourses[enum] = collect_data(module_tds, 1, False)

    data ={
        'promotion_resourses': promotion_resources,
        'skils_resourses': skils_resourses,
        'modeules_resourses': modeules_resourses,
    }

    return data

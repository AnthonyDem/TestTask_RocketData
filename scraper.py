import json
from bs4 import BeautifulSoup
from Load_data_fron_site import SaverMebel, SaverTui
from bs4.element import Tag
import lxml
import xmltodict
from Convert_data import JSONConvertMebelShara, JSONConvertTuiRu

url1 = 'https://www.mebelshara.ru/contacts'
url2 = 'https://www.tui.ru/api/office/list/?cityId=1&subwayId=&hoursFrom=&hoursTo=&serviceIds=all&toBeOpenOnHolidays=false'


def make_dict(city_name: str, shop: Tag):
    return {
        'address': city_name + ', ' + shop['data-shop-address'],
        'latlon': [float(shop['data-shop-latitude']), float(shop['data-shop-longitude'])],
        'name': 'Мебель Шара',
        'phones': ['8 800 551 06 10'],
        'working_hours': [shop['data-shop-mode1'], shop['data-shop-mode2']],
    }


def make_tui_right_dict():
    tui = []
    file = load()
    for i in file:
        phones = i.get('phones')
        working_hours_weekdays = i.get('hoursOfOperation').get('workdays')
        working_hours_weekends = i.get('hoursOfOperation').get('saturday')
        if working_hours_weekends.get('startStr') is None:
            di = {'address': i.get('address'), 'latlon': [i.get('latitude'), i.get('longitude')], 'name': i.get('name'),
                  'phones': [i.get('phone') for i in phones],
                  'working_days': ["пн-вс " + working_hours_weekdays.get('startStr') + " до " +
                                   working_hours_weekdays.get('endStr'), "сб-вс: Выходной"]}

        else:
            di = {'address': i.get('address'), 'latlon': [i.get('latitude'), i.get('longitude')], 'name': i.get('name'),
                  'phones': [i.get('phone') for i in phones],
                  'working_days': ["пн-вс " + working_hours_weekdays.get('startStr') + " до " +
                                   working_hours_weekdays.get('endStr'), "сб-вс " +
                                   working_hours_weekends.get('startStr') + '-' + working_hours_weekends.get('endStr')]}
        tui.append(di)
    return tui


def load():
    with open('tuiru.json', 'r') as f:
        json_data = json.load(f)
        return json_data


def city_shops(city_div: Tag):
    city_tag = city_div.find('h4', {'class': 'js-city-name'}).extract()
    city_name = city_tag.text

    shops = city_div.find_all('div', {'class': 'shop-list-item'})

    return [make_dict(city_name, shop) for shop in shops]


def main():
    saver = SaverMebel(url1)
    saver.save()
    saver = SaverTui(url2)
    saver.save()
    html1 = open('mebelshara.html').read()
    js_out = make_tui_right_dict()
    soup = BeautifulSoup(html1, 'lxml')
    cities = soup.find_all('div', {'class': 'city-item'})
    shop_list = []

    for city in cities:
        shop_list += city_shops(city)

    conv_tui = JSONConvertTuiRu()
    conv_tui.write(data=js_out)

    conv_mebel = JSONConvertMebelShara()
    conv_mebel.write(data=shop_list)


'''def argparser():
    parser = argparse.ArgumentParser("Parse data from web-sites")

    parser.add_argument('url', type=str, help='enter path to site')

    parser.add_argument('filename', type=str, help='enter filename')
    return parser'''

if __name__ == '__main__':
    main()

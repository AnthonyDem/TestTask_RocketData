from bs4 import BeautifulSoup
from Load_data_fron_site import SaverMebel, SaverTui
from bs4.element import Tag
import lxml

url1 = 'https://www.mebelshara.ru/contacts'
url2 = 'https://www.tui.ru/offices/'


def make_dict(city_name: str, shop: Tag):
    return {
        'address': city_name + ', ' + shop['data-shop-address'],
        'latlon': [shop['data-shop-latitude'], shop['data-shop-longitude']],
        'name': 'Мебель Шара',
        'phones': ['8 800 551 06 10'],
        'working_hours': [shop['data-shop-mode1'], shop['data-shop-mode2']],
    }


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


'''def argparser():
    parser = argparse.ArgumentParser("Parse data from web-sites")

    parser.add_argument('url', type=str, help='enter path to site')

    parser.add_argument('filename', type=str, help='enter filename')
    return parser'''

if __name__ == '__main__':
    html1 = open('mebelshara.html').read()
    html2 = open('tuiru.html').read()
    soup = BeautifulSoup(html1, 'lxml')
    cities = soup.find_all('div', {'class': 'city-item'})

    shop_list = []

    for city in cities:
        shop_list += city_shops(city)

    print(shop_list)


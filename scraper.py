from bs4 import BeautifulSoup
from Load_data_fron_site import SaverMebel, SaverTui
import argparse


url1 = 'https://www.mebelshara.ru/contacts'
url2 = 'https://www.tui.ru/offices/'


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
    # parser = argparser()
    # args = parser.parse_args()
    main()



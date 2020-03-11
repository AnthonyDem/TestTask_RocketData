import json
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup

class Converter(ABC):
    @abstractmethod
    def write(self, data, filename):
        pass


class JSONConvert(Converter):
    def write(self, data, filename):
        html1 = open('mebelshara.html').read()
        soup = BeautifulSoup(html1, 'lxml')
        div = soup.find('dic', {'class':'adress'})
        with open(filename, 'w') as f:
            f.write(json.dumps({
                'adress':
            }))

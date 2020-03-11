import requests
from abc import ABC, abstractmethod


class Saver(ABC):
    @abstractmethod
    def save(self):
        pass


class SaverMebel(Saver):
    def __init__(self, url):
        self.url = url

    def save(self):
        r = requests.get(self.url)
        r.encoding = 'utf-8'
        with open('mebelshara.html', 'w') as f:
            f.write(r.text)


class SaverTui(Saver):
    def __init__(self, url):
        self.url = url

    def save(self):
        r = requests.get(self.url)
        r.encoding = 'utf-8'
        with open('tuiru.html', 'w') as f:
            f.write(r.text)

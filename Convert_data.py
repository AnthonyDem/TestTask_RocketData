import json
from abc import ABC, abstractmethod


class Converter(ABC):
    @abstractmethod
    def write(self, data):
        pass


class JSONConvertMebelShara(Converter):
    def write(self, data):
        with open('MebelShara.json', 'w') as f:
            f.write(json.dumps(data, indent=2, ensure_ascii=False))


class JSONConvertTuiRu(Converter):
    def write(self, data):
        with open('TuiRu.json', 'w') as f:
            f.write(json.dumps(data, indent=2, ensure_ascii=False))

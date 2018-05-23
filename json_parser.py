import json


class ParsedData:
    def __init__(self):
        self.figures = []
        self.bg_color = ""
        self.fg_color = ""
        self.width = 0
        self.height = 0
        self.pallet = {}


class JsonParser():
    def __init__(self):
        self.parsed_data = ParsedData()

    def parse_json(self,path):
        with open(path) as f:
            data = json.load(f)
        self.parsed_data.figures = data['Figures']
        self.parsed_data.bg_color = data['Screen']['bg_color']
        self.parsed_data.fg_color = data['Screen']['fg_color']
        self.parsed_data.width = data['Screen']['width']
        self.parsed_data.height = data['Screen']['height']
        self.parsed_data.pallet = data['Palette']
        return self.parsed_data


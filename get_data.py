import json


class GetData:
    @staticmethod
    def data_json(file): # "competitors2.json"
        with open(file, "r", encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data

    @staticmethod
    def data_txt(file): # "results_RUN.txt"
        with open(file, "r", encoding='utf-8') as txt_file:
            data = txt_file.readlines()
        return data

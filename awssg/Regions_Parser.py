import json
from awssg.Parser_Interface import Parser_Interface

class Regions_Parser(Parser_Interface):

    def set_string_data(self, string_data: str):
        self.data = json.loads(string_data)


    def set_data(self, data: dict):
        self.data = data


    def get_list(self) -> list:
        region_list = []

        for chuck in self.data["Regions"]:
            region_list.append(chuck["RegionName"])

        return region_list


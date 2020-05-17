from src.Parser_Interface import Parser_Interface

class Regions_Parser(Parser_Interface):

    def set_data(self, data: dict):
        self.data = data


    def list(self) -> list:
        region_list = []

        for chuck in self.data["Regions"]:
            region_list.append(chuck["RegionName"])

        return region_list


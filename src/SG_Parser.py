import json
from src.SG import SG
from src.Parser_Interface import Parser_Interface

class SG_Parser(Parser_Interface):

    def set_string_data(self, string_data: str):
        self.data = json.loads(string_data)
        return self


    def set_data(self, data: dict):
        self.data = data
        return self


    def list(self) -> list:

        sg_list = []

        for chunk in self.data["SecurityGroups"]:

            sg = SG()
            sg.set_data(chunk)

            sg_list.append(sg)

        return sg_list

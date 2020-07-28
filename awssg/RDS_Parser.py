import json
from awssg.RDS import RDS
from awssg.Parser_Interface import Parser_Interface

class RDS_Parser(Parser_Interface):

    def __init__(self):
        self.rds_list = []
        self.list_parsed = False


    def set_string_data(self, string_data: str):
        self.data = json.loads(string_data)
        return self


    def set_data(self, data: dict):
        self.data = data
        self.make_list()
        return self


    def is_list_parsed(self):
        return self.list_parsed


    def is_element_exists(self, element_name: str) -> bool:

        for rds_item in self.rds_list:
            if rds_item.get_name() == element_name:
                return True

        return False


    def get_list(self) -> list:
        return self.rds_list


    def make_list(self) -> Parser_Interface:

        for rds_raw_data in self.data["DBInstances"]:
            rds = RDS()
            rds.set_data(rds_raw_data)
            self.rds_list.append(rds)

        self.list_parsed = True

        return self

    
    def get_rds_by_name(self, name: str) -> RDS:
        for rds in self.rds_list:
            if rds.get_name() == name:
                return rds
        raise Exception("There are no RDS with the given name.")

        

import json
from awssg.SG import SG
from awssg.RDS_Parser import RDS_Parser
from awssg.Parser_Interface import Parser_Interface
from awssg.Client_Interface import Client_Interface

class SG_Parser(Parser_Interface):

    def __init__(self):
        self.list = []


    def set_string_data(self, string_data: str):
        self.data = json.loads(string_data)
        self.make_list()
        return self


    def set_data(self, data: dict):
        self.data = data
        self.make_list()
        return self


    def get_list(self) -> list:
        return self.list


    def make_list(self):

        for chunk in self.data["SecurityGroups"]:

            sg = SG()
            sg.set_data(chunk)

            self.list.append(sg)


    def is_rds_instance_name_exists(self, rds_instance_name, client: Client_Interface) -> bool:

        rds_parser = RDS_Parser()
        rds_data = client.describe_db_instances()
        rds_parser.set_data(rds_data)

        rds_list = rds_parser.get_list()

        for sg in rds_list:
            if sg.get_name() == rds_instance_name:
                return True

        return False

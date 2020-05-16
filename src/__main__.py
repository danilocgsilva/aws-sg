from src.Client_Config import Client_Config
from src.Fetcher import Fetcher
from src.SG_Parser import SG_Parser

def main():

    client_config = Client_Config()
    client = client_config.get_client()

    fetcher = Fetcher()
    fetcher.set_client(client)

    sg_parser = SG_Parser()
    sgs_data = fetcher.sgs_data()
    sg_parser.set_data(sgs_data)
    security_group_list = sg_parser.list()

    for sg in security_group_list:
        print(sg.get_name())
    
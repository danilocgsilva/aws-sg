from src.Fetcher import Fetcher
from src.SG_Parser import SG_Parser
import argparse

def print_single_region_data(region: str, client_config: str):

    client_config.set_region(region)

    client = client_config.get_client()

    fetcher = Fetcher()
    fetcher.set_client(client)

    sg_parser = SG_Parser()
    sgs_data = fetcher.sgs_data()
    sg_parser.set_data(sgs_data)
    security_group_list = sg_parser.list()

    for sg in security_group_list:
        print(sg.get_name())


def fast_add_arguments(arguments: list, parser):

    for argument in arguments:
        parser.add_argument(
            argument[0],
            argument[1],
            type=str,
            required=False
        )        

    return parser


def get_regions(client_config) -> list:
    

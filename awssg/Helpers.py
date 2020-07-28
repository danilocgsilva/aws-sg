from src.Fetcher import Fetcher
from src.SG_Parser import SG_Parser
from src.Client import Client
from src.Client_Config import Client_Config
from src.Client_Config_Interface import Client_Config_Interface
from src.Regions_Parser import Regions_Parser
from src.RDS import RDS
from src.RDS_Parser import RDS_Parser
import argparse

def readable_single_region_data(region: str, client_config: Client_Config_Interface) -> str:

    client_config.set_region(region)

    client = client_config.get_client()

    fetcher = Fetcher().set_client(client)

    sg_parser = SG_Parser()
    sgs_data = fetcher.get_sgs_data()
    sg_parser.set_data(sgs_data)
    security_group_list = sg_parser.get_list()

    readable_string = ""
    for sg in security_group_list:
        readable_string += "\n" + sg.get_name()

    return readable_string


def fast_add_arguments(arguments: list, parser):

    for argument in arguments:
        parser.add_argument(
            argument[0],
            argument[1],
            type=str,
            required=False
        )        

    return parser


def get_regions(client: Client) -> list:
    regions_parser = Regions_Parser()
    regions_parser.set_data(client.describe_regions())
    return regions_parser.get_list()


def readable_loop_regions_securities_groups(client_config: Client_Config) -> str:
    regions = get_regions(client_config.get_client())
    readable_string = ""
    for region in regions:
        readable_string += readable_single_region_data(region, client_config)
    return readable_string


def print_securities_groups(args, client_config):
    if args.region is not None:
        print(readable_single_region_data(args.region, client_config))
    else:
        print(readable_loop_regions_securities_groups(client_config))


def print_securities_groups_from_rds_instance(rds_name):
    
    fetcher = Fetcher().set_client(Client())
    rds_data = fetcher.get_rds_data(rds_name)
    rds_parser = RDS_Parser().set_data(rds_data)

    if not rds_parser.is_element_exists(rds_name):
        print('There\'s no instance with name ' + rds_name)
    else:
        rds = rds_parser.get_rds_by_name(rds_name)
        print("Securities groups for " + rds_name)
        for sg_name in rds.get_securities_groups_names():
            print("\t" + sg_name)


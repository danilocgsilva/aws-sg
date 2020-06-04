import sys
import argparse
sys.path.insert(1, '..')
from src.Client_Config import Client_Config
from src.Fetcher import Fetcher
from src.Helpers import fast_add_arguments

client_config = Client_Config()

arguments_list = [
    ['--profile', '-p'],
    ['--region', '-r'],
    ['--name', '-n']
]

parser = argparse.ArgumentParser()
parser = fast_add_arguments(arguments_list, parser)
args = parser.parse_args()

if args.name == None:
    print("You must provides the security group id: --name or -n")
    exit()

if args.profile is not None:
    client_config.set_profile(args.profile)

if args.region is not None:
    client_config.set_region(args.region)

security_groups_data = Fetcher()\
    .set_client(client_config.get_client())\
    .get_sgs_data_by_name(args.name)

print(security_groups_data)

from src.Client_Config import Client_Config
from src.Helpers import fast_add_arguments
from src.Fetcher import Fetcher
import argparse

client_config = Client_Config()

arguments_list = [
    ['--profile', '-p'],
    ['--region', '-r']
]
parser = argparse.ArgumentParser()
parser = fast_add_arguments(arguments_list, parser)
args = parser.parse_args()


if args.profile is not None:
    client_config.set_profile(args.profile)

if args.region is not None:
    client_config.set_region(args.region)

fetcher = Fetcher()
fetcher.set_client(client_config.get_client())
print(fetcher.get_all_regions_data())

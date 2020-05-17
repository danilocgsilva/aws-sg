from src.Client_Config import Client_Config
from src.Helpers import print_single_region_data, fast_add_arguments, get_regions
import argparse

def main():

    arguments_list = [
        ['--profile', '-p'],
        ['--region', '-r']
    ]

    parser = argparse.ArgumentParser()
    parser = fast_add_arguments(arguments_list, parser)
    args = parser.parse_args()

    client_config = Client_Config()

    if args.profile is not None:
        client_config.set_profile(args.profile)

    if args.region is not None:
        print_single_region_data(args.region, client_config)
    else:
        regions = get_regions(client_config)


    
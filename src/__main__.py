from src.Client_Config import Client_Config
from src.Helpers import print_single_region_data,\
    fast_add_arguments, \
    get_regions, \
    print_loop_regions_securities_groups, \
    print_regions_without_rds, \
    print_securities_groups_from_rds_instance
import argparse

def main():

    arguments_list = [
        [ '--profile', '-p' ],
        [ '--region', '-r' ],
        [ '--rds', '-rds' ]
    ]

    parser = argparse.ArgumentParser()
    parser = fast_add_arguments(arguments_list, parser)
    args = parser.parse_args()


    if args.rds is not None:
        print_securities_groups_from_rds_instance(args.rds)
    else:
        client_config = Client_Config()
        if args.profile is not None:
            client_config.set_profile(args.profile)
        print_regions_without_rds(args, client_config)


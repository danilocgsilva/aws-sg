from awssg.Client_Config import Client_Config
from awssg.Helpers import fast_add_arguments, \
    get_regions, \
    print_securities_groups, \
    print_securities_groups_from_rds_instance, \
    create_sg, \
    list_sg, \
    get_hash_date_from_date
import argparse
import datetime


def main():

    arguments_list = [
        [ '--profile', '-p' ],
        [ '--region', '-r' ],
        [ '--rds', '-rds' ],
        [ '--create', '-c' ]
    ]

    parser = argparse.ArgumentParser()
    parser = fast_add_arguments(arguments_list, parser)
    args = parser.parse_args()

    client_config = Client_Config()

    if args.profile:
        client_config.set_profile(args.profile)

    if args.region:
        client_config.set_region(args.region)

    if args.create:
        group_name = args.create + get_hash_date_from_date(datetime.datetime.now())
        create_sg(group_name_description=group_name)
    else:
        list_sg(args, client_config)

    
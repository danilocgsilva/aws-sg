from awssg.Client_Config import Client_Config
from awssg.Helpers import fast_add_arguments, \
    list_sg, \
    create_sg, \
    get_rules_from
from awssg.SG_Client import SG_Client
from awssg.Client import Client
from awssg.Fetcher import Fetcher
from awssg.SG_Parser import SG_Parser
import argparse


def main():
    arguments_list = [
        ['--profile', '-p'],
        ['--region', '-r'],
        ['--rds', '-rds'],
        ['--create', '-c'],
        ['--delete', '-d'],
        ['--protocol', '-pr'],
        ['--ip', '-i'],
        ['--port', '-po'],
        ['--rules-from', '-rf'],
        ['--fields', '-f']
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
        create_sg(args)
    elif args.delete:
        ec2 = Client()
        SG_Client().set_client(ec2).set_group_name(args.delete).delete_sg()
    elif args.rules_from:
        get_rules_from(client_config, args)
    else:
        list_sg(args, client_config)

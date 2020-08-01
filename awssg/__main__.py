from awssg.Client_Config import Client_Config
from awssg.Helpers import fast_add_arguments, \
    list_sg, \
    create_sg
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
        ['--rules-from', '-rf']
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
        client = client_config.get_client()
        fetcher = Fetcher().set_client(client)
        sg_parser = SG_Parser()
        sgs_data = fetcher.get_sgs_data_by_id(args.rules_from)
        sg_parser.set_data(sgs_data)
        sg = sg_parser.get_sg()
        print("Your security group have following rules:")
        for rule in sg.get_rules():
            print(
                " * Protocol: " + rule.get_protocol() + ", ip: " + str(rule.get_ip()) + ", port: " + str(rule.get_port())
            )
    else:
        list_sg(args, client_config)

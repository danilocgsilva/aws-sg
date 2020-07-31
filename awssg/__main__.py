from awssg.Client_Config import Client_Config
from awssg.Helpers import fast_add_arguments, \
    list_sg, \
    get_hash_date_from_date
from awssg.SG_Client import SG_Client
from awssg.Client import Client
from awssg.Fetcher import Fetcher
from awssg.SG_Parser import SG_Parser
import argparse
import datetime


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
        group_name = args.create + get_hash_date_from_date(datetime.datetime.now())
        ec2 = Client()
        sg_client = SG_Client()
        result = sg_client.set_client(ec2).set_group_name(group_name).create_sg()

        print("Security group named " + group_name + " has just been created.")

        if args.protocol and args.ip and args.port:
            sg_client.set_rule(result["GroupId"], args.protocol, args.ip, args.port)

    elif args.delete:
        ec2 = Client()
        SG_Client().set_client(ec2).set_group_name(args.delete).delete_sg()
    elif args.rules_from:
        #ec2 = Client()
        #sg = SG()
        #sg.set_string_data()
        #rules = sg.get_rules()
        #print("The security group named " + sg.get_name() + " have the following rules: ")
        #for rule in sg.get_rules():
        #    print("Protocol: " + rule.get_protocol() + ", ip: " + rule.get_ip() + ", port: " + rule.get_port())

        client = client_config.get_client()
        fetcher = Fetcher().set_client(client)
        sg_parser = SG_Parser()
        sgs_data = fetcher.get_sgs_data_by_id(args.rules_from)
        sg_parser.set_data(sgs_data)
    else:
        list_sg(args, client_config)

import sys
import argparse
sys.path.insert(1, '..')
from awssg.Client_Config import Client_Config
from awssg.Helpers import fast_add_arguments
from awssg.Client import Client

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

vpcs_data = Client()\
    .describe_vpcs()

print(vpcs_data)
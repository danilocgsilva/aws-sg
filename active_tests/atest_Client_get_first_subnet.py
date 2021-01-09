from awssg.Client import Client
from awssg.Helpers import fast_add_arguments
from awssg.Client_Config import Client_Config
import argparse
import os

arguments_list = [
    ['--profile', '-p'],
    ['--region', '-r'],
    ['--vpc', '-v']
]

parser = argparse.ArgumentParser()
parser = fast_add_arguments(arguments_list, parser)
args = parser.parse_args()

if not args.profile:
    print("You need run this script with a profile name complementing the command with -p <profile_name> or --profile <profile_name>")
    exit()

if not args.region:    
    print("You need run this script with a region name complementing the command with -r <region_name> or --region <region_name>")
    exit()

if not args.vpc:
    print("You need run this script with a vpc id name complementing the command with -v <vpc_id> or --vpc <vpc_id>")
    exit()

os.environ["AWS_PROFILE"] = args.profile

Client_Config().set_region(args.region)

client = Client()

results = client.getSubnetId(args.vpc)

print(results)


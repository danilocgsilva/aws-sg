from awssg.VPC_Client import VPC_Client
from awssg.Helpers import fast_add_arguments
from awssg.Client_Config import Client_Config
from danilocgsilvame_python_helpers.DcgsPythonHelpers import DcgsPythonHelpers
import argparse
import os

args = DcgsPythonHelpers().command_line_argument_names(
    'profile', 'p',
    'region', 'r',
    'vpc', 'v'
)

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

vpc_client = VPC_Client()

results = vpc_client.get_first_subnet(args.vpc)

print(results)


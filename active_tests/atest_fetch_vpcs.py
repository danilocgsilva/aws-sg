import sys
import argparse
import os
sys.path.insert(1, '..')
from awssg.Client_Config import Client_Config
from awssg.Helpers import fast_add_arguments
from awssg.Client import Client
from danilocgsilvame_python_helpers.DcgsPythonHelpers import DcgsPythonHelpers

args = DcgsPythonHelpers().command_line_argument_names(
    'region', 'r',
    'profile', 'p'
)

if not args.profile:
    print("You must specify a profile name with --profile or -p argument in commando line.")
    exit()

os.environ["AWS_PROFILE"] = args.profile

client_config = Client_Config()

if args.profile is not None:
    client_config.set_profile(args.profile)

if args.region is not None:
    client_config.set_region(args.region)

vpcs_data = Client().describe_vpcs()

print(vpcs_data)
from awssg.Client_Config import Client_Config
from awssg.VPC_Client import VPC_Client
from danilocgsilvame_python_helpers.DcgsPythonHelpers import DcgsPythonHelpers
import os

args = DcgsPythonHelpers().command_line_argument_names(
    'region', 'r',
    'profile', 'p'
)

if not args.region:
    print("You need to specify a region with --region <region-name> or -r <region-name> after script.")
    exit()

if not args.profile:
    print("You need to specify a profile with --profile <profile-name> or -p <profile-name> after script.")
    exit()

os.environ["AWS_PROFILE"] = args.profile

Client_Config().set_region(args.region)

client = VPC_Client()
results = client.fetch_vpcs_list_names()

for result in results:
    print(" * " + result)

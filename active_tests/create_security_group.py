import sys
import argparse
import boto3
sys.path.insert(1, '..')
from danilocgsilvame_python_helpers.DcgsPythonHelpers import DcgsPythonHelpers
from awssg.Helpers import fast_add_arguments
import os

args = DcgsPythonHelpers().command_line_argument_names(
    'profile', 'p',
    'region', 'r',
    'name', 'n'
)

if args.name == None:
    print("The command has been stoped. You need to provides a name for security group thorugh -n or --name parameter.")
    exit()

if args.profile:
    os.environ["AWS_PROFILE"] = args.profile

print("This action will create a real security group in your infraestructure, just to show the output results.")
response = input("Are you sure to do so? Type yes. Otherwise, the action will be canceled: ")
if not response == "yes":
    print("Cancelling...")
    exit()

boto3Client = boto3.client('ec2', region_name=args.region)

security_group_name_to_create = args.name

vpcs_response = boto3Client.describe_vpcs()
vpcs_containers = vpcs_response.get('Vpcs', [{}])

results = boto3Client.create_security_group(
    GroupName=security_group_name_to_create,
    Description=security_group_name_to_create,
    VpcId=vpcs_containers[0].get('VpcId', '')
)

print(results)

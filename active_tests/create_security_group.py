import sys
import argparse
import boto3
sys.path.insert(1, '..')
# from awssg.Client_Config import Client_Config
from awssg.Helpers import fast_add_arguments
import os

print("This action will create a real security group in your infraestructure, just to show the output results.")
response = input("Are you sure to do so? Type yes. Otherwise, the action will be canceled: ")
if not response == "yes":
    print("Cancelling...")
    exit()

# client_config = Client_Config()

arguments_list = [
    ['--profile', '-p'],
    ['--region', '-r'],
    ['--name', '-n']
]

parser = argparse.ArgumentParser()
parser = fast_add_arguments(arguments_list, parser)
args = parser.parse_args()

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

client_config = Client_Config()

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

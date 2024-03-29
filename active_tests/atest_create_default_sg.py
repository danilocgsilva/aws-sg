from awssg.Client import Client
from awssg.Helpers import fast_add_arguments
from awssg.SG_Client import SG_Client
from awssg.Client_Config import Client_Config
from danilocgsilvame_python_helpers.DcgsPythonHelpers import DcgsPythonHelpers
from dcgsasklist.Ask import Ask
from dcgsasklist.AskException import AskException
import datetime
import argparse
import os

arguments_list = [
    ['--profile', '-p'],
    ['--region', '-r'],
    ['--name', '-n']
]

parser = argparse.ArgumentParser()
parser = fast_add_arguments(arguments_list, parser)
args = parser.parse_args()

if args.profile:
    os.environ["AWS_PROFILE"] = args.profile

if args.name == None:
    print("The command has been stoped. You need to provides a name for security group thorugh -n or --name parameter.")
    exit()

print("This action will create a real security group in your infraestructure, just to show the output results.")
response = input("Are you sure to do so? Type yes. Otherwise, the action will be canceled: ")

if not response == "yes":
    print("Cancelling...")
    exit()

client_config = Client_Config()

if args.region:
    client_config.set_region(args.region)

ec2 = Client()
sg_client = SG_Client()
sg_client.set_client(ec2).set_group_name(args.name)
if sg_client.is_multiples_vpcs():
    ask = Ask( sg_client.fetch_vpcs_list_names() )
    vpc_choosed = None
    try:
        vpc_choosed = ask.ask("Which vpc do you would like to setup the security group?:")
    except AskException:
        print("You choosed an invalid option. Quiting, nothing done.")
        exit()
    sg_client.set_vpc(vpc_choosed)

results_creation = sg_client.create_default_sg()
print(results_creation)
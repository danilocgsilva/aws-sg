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

vpc_client = VPC_Client()
first_vpc_name = vpc_client.get_first_vpc_name()
print(first_vpc_name)

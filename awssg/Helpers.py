from awssg.Fetcher import Fetcher
from awssg.SG_Parser import SG_Parser
from awssg.Client import Client
from awssg.Client_Config import Client_Config
from awssg.Client_Config_Interface import Client_Config_Interface
from awssg.Regions_Parser import Regions_Parser
from awssg.RDS import RDS
from awssg.RDS_Parser import RDS_Parser
import argparse
import boto3


def readable_single_region_data(region: str, client_config: Client_Config_Interface) -> str:

    client_config.set_region(region)

    client = client_config.get_client()

    fetcher = Fetcher().set_client(client)

    sg_parser = SG_Parser()
    sgs_data = fetcher.get_sgs_data()
    sg_parser.set_data(sgs_data)
    security_group_list = sg_parser.get_list()

    readable_string = ""
    for sg in security_group_list:
        readable_string += " * " + sg.get_name() + "\n"

    return readable_string


def fast_add_arguments(arguments: list, parser):

    for argument in arguments:
        parser.add_argument(
            argument[0],
            argument[1],
            type=str,
            required=False
        )        

    return parser


def get_regions(client: Client) -> list:
    regions_parser = Regions_Parser()
    regions_parser.set_data(client.describe_regions())
    return regions_parser.get_list()


def readable_loop_regions_securities_groups(client_config: Client_Config) -> str:
    regions = get_regions(client_config.get_client())
    for region in regions:
        print("Region: " + region)
        print(readable_single_region_data(region, client_config))


def print_securities_groups(args, client_config):
    if args.region:
        print(readable_single_region_data(args.region, client_config))
    else:
        readable_loop_regions_securities_groups(client_config)


def print_securities_groups_from_rds_instance(rds_name):
    
    fetcher = Fetcher().set_client(Client())
    rds_data = fetcher.get_rds_data(rds_name)
    rds_parser = RDS_Parser().set_data(rds_data)

    if not rds_parser.is_element_exists(rds_name):
        print('There\'s no instance with name ' + rds_name)
    else:
        rds = rds_parser.get_rds_by_name(rds_name)
        print("Securities groups for " + rds_name)
        for sg_name in rds.get_securities_groups_names():
            print("\t" + sg_name)


def create_sg(group_name_description):
    ec2 = boto3.client('ec2')
    vpcs_response = ec2.describe_vpcs()
    vpc_id = vpcs_response.get('Vpcs', [{}])[0].get('VpcId', '')
    ec2.create_security_group(
        GroupName=group_name_description, 
        Description=group_name_description, 
        VpcId=vpc_id
    )
    print("Security group " + group_name_description + " has been just created in " + ec2.meta.region_name + ".")


def get_hash_date_from_date(datetime):
    return str(datetime.year) + '{0:02}'.format(datetime.month) + '{0:02}'.format(datetime.day) + '-' + '{0:02}'.format(datetime.hour) + 'h' + '{0:02}'.format(datetime.minute) + 'm' + '{0:02}'.format(datetime.second) + 's' + str(datetime.microsecond)


def list_sg(args, client_config):
    if args.rds is not None:
        print_securities_groups_from_rds_instance(args.rds)
    else:
        print_securities_groups(args, client_config)

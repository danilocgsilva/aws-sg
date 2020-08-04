from awssg.Fetcher import Fetcher
from awssg.SG_Parser import SG_Parser
from awssg.Client import Client
from awssg.Client_Config import Client_Config
from awssg.Client_Config_Interface import Client_Config_Interface
from awssg.Regions_Parser import Regions_Parser
from awssg.SG_Client import SG_Client
from awssg.RDS_Parser import RDS_Parser
from awssg.Printer import Printer
import datetime


def readable_single_region_data(region: str, client_config: Client_Config_Interface, fields = None) -> str:
    client_config.set_region(region)
    client = client_config.get_client()
    fetcher = Fetcher().set_client(client)
    sg_parser = SG_Parser()
    sgs_data = fetcher.get_sgs_data()
    sg_parser.set_data(sgs_data)
    security_group_list = sg_parser.get_list()

    readable_string = ""
    for sg in security_group_list:
        readable_string += Printer().set_sg(sg).set_fields(fields).get_string() + "\n"

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


def readable_loop_regions_securities_groups(client_config: Client_Config, fields: str) -> str:
    regions = get_regions(client_config.get_client())
    for region in regions:
        print("Region: " + region)
        print(readable_single_region_data(region, client_config))


def print_securities_groups(args, client_config):
    if args.region:
        print(readable_single_region_data(args.region, client_config, args.fields))
    else:
        readable_loop_regions_securities_groups(client_config, args.fields)


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


def get_hash_date_from_date(datetime_data):
    return str(datetime_data.year) + '{0:02}'.format(datetime_data.month) + '{0:02}'.format(datetime_data.day) + '-' + '{0:02}'.format(datetime_data.hour) + 'h' + '{0:02}'.format(datetime_data.minute) + 'm' + '{0:02}'.format(datetime_data.second) + 's' + str(datetime_data.microsecond)


def list_sg(args, client_config):
    if args.rds is not None:
        print_securities_groups_from_rds_instance(args.rds)
    else:
        print_securities_groups(args, client_config)


def create_sg(args):
    group_name = args.create + get_hash_date_from_date(datetime.datetime.now())
    ec2 = Client()
    sg_client = SG_Client()
    result = sg_client.set_client(ec2).set_group_name(group_name).create_sg()
    print("Security group named " + group_name + " has just been created.")
    if args.protocol and args.ip and args.port:
        sg_client.set_rule(result["GroupId"], args.protocol, args.ip, args.port)


def get_rules_from(client_config, args):
    client = client_config.get_client()
    fetcher = Fetcher().set_client(client)
    sg_parser = SG_Parser()
    sgs_data = fetcher.get_sgs_data_by_id(args.rules_from)
    sg_parser.set_data(sgs_data)
    sg = sg_parser.get_sg()
    print("Your security group have following rules:")
    for rule in sg.get_rules():
        print(
            " * Protocol: " + rule.get_protocol() + ", ip: " + str(rule.get_ip()) + ", port: " + str(rule.get_port())
        )

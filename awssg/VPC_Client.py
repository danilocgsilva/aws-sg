import boto3
from cli_ask.Ask import Ask

class VPC_Client:

    def __init__(self, ec2_client=None):
        self.vpcs_data = None
        if not ec2_client:
            self.ec2_client = boto3.client('ec2')
        else:
            self.ec2_client = ec2_client

    def set_ec2_client(self, ec2_client):
        self.ec2_client = ec2_client

    def get_first_subnet(self, vpc_id):

        if not vpc_id:
            raise Exception("The vpc value must not be None.")

        subnets = self.ec2_client.describe_subnets(
            Filters=[{
                "Name": "vpc-id",
                "Values": [vpc_id]
            }]
        )

        if len(subnets["Subnets"]) == 0:
            raise Exception("The current vpc does not have any subnet.")

        return subnets["Subnets"][0]["SubnetId"]

    def is_multiples_vpcs(self) -> bool:
        self.__fill_vpc_data_if_empty()
        vpcs_count = len(self.vpcs_data["Vpcs"])
        if vpcs_count > 1:
            return True
        elif vpcs_count == 1:
            return False
        else:
            raise Exception("The account have no Vpc!")

    def fetch_vpcs_list_names(self) -> list:
        self.__fill_vpc_data_if_empty()

        return list(
            map(lambda item : item["VpcId"], self.vpcs_data["Vpcs"])
        )

    def describe_vpcs(self):
        self.__fill_vpc_data_if_empty()
        return self.vpcs_data

    def get_first_vpc_name(self) -> str:
        self.__fill_vpc_data_if_empty()
        first_vpc = self.vpcs_data["Vpcs"][0]["VpcId"]
        if first_vpc == None:
            raise Exception("Sorry, I could not discover the first vpc name.")
        return first_vpc

    def vpc_exists(self, vpc_id: str) -> bool:
        vpcs_strings = self.fetch_vpcs_list_names()
        return vpc_id in vpcs_strings

    def __fill_vpc_data_if_empty(self):
        if self.vpcs_data == None:
            self.vpcs_data = self.ec2_client.describe_vpcs()

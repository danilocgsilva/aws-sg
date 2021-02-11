import boto3
from dcgsasklist.Ask import Ask

class VPC_Client:

    def __init__(self):
        self.vpcs_data = None
        self.ec2_client = boto3.client('ec2')

    def get_first_subnet(self, vpc_id):

        if not vpc_id:
            raise Exception("The vpc value must not be None.")

        subnets = self.ec2_client.describe_subnets(
            Filters=[{
                "Name": "vpc-id",
                "Values": [vpc_id]
            }]
        )

        if not len(subnets["Subnets"]) == 1:

            subnet_names = []
            for singleSubnet in subnets["Subnets"]:
                subnet_names.append(singleSubnet["SubnetId"])
            ask = Ask(subnet_names)
            subnet = ask.ask("There are multiples subnets in your VPC. Type what subnet did you desire: ")
        else:
            subnet = subnets["Subnets"][0]["SubnetId"]

        return subnet

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

    def __fill_vpc_data_if_empty(self):
        if self.vpcs_data == None:
            self.vpcs_data = self.ec2_client.describe_vpcs()

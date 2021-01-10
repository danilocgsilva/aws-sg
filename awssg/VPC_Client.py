import boto3

class VPC_Client:

    def __init__(self):
        self.vpcs_data = None
        self.ec2_client = boto3.client('ec2')

    def get_first_subnet(self, vpc_id):
        subnets = self.ec2_client.describe_subnets(
            Filters=[{
                "Name": "vpc-id",
                "Values": [vpc_id]
            }]
        )

        if not len(subnets["Subnets"]) == 1:
            raise Exception("This vpc has multiples subnets and cannod handle this situation.")

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

    def __fill_vpc_data_if_empty(self):
        if self.vpcs_data == None:
            self.vpcs_data = self.ec2_client.describe_vpcs()

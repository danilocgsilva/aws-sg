from awssg.Client_Interface import Client_Interface
import boto3

class Client(Client_Interface):

    def __init__(self):
         self.ec2_client = boto3.client('ec2')
         self.vpcs_data = None

    def describe_security_groups(self) -> dict:
        return self.ec2_client.describe_security_groups()

    def describe_regions(self) -> dict:
        return self.ec2_client.describe_regions()

    def describe_db_instances(self) -> dict:
        self.aws_client = boto3.client('rds')
        return self.aws_client.describe_db_instances()

    def describe_specific_security_group(self, security_group: str):
        return self.ec2_client.describe_security_groups(GroupNames=[security_group])

    def describe_vpcs(self) -> dict:
        self.__fill_vpc_data_if_empty()
        return self.vpcs_data

    def create_security_group(self, group_name: str, vpc_id: str):
        return self.ec2_client.create_security_group(
            GroupName=group_name,
            Description=group_name,
            VpcId=vpc_id
        )

    def get_region_name(self) -> str:
        return self.ec2_client.meta.region_name

    def delete_security_group_by_name(self, group_name: str):
        self.ec2_client.delete_security_group(
            GroupName=group_name
        )
    
    def delete_security_group_by_id(self, group_id: str):
        self.ec2_client.delete_security_group(
            GroupId=group_id
        )

    def set_rule(self, group_id: str, protocol: str, ip: str, port: str):

        ec2 = boto3.resource('ec2')
        security_group = ec2.SecurityGroup(group_id)

        security_group.authorize_ingress(
            IpProtocol=protocol,
            CidrIp=ip + "/32",
            FromPort=int(port),
            ToPort=int(port)
        )

    def describe_specific_security_group_by_id(self, sg_id: str):
        return self.ec2_client.describe_security_groups(GroupIds=[sg_id])

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

    def __fill_vpc_data_if_empty(self):
        if self.vpcs_data != None:
            self.vpcs_data = self.ec2_client.describe_vpcs()
        


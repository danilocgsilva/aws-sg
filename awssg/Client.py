from awssg.Client_Interface import Client_Interface
import boto3

class Client(Client_Interface):

    def __init__(self):
         self.ec2_client = boto3.client('ec2')

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
        return self.ec2_client.describe_vpcs()

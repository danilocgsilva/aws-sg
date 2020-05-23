from src.Client_Interface import Client_Interface
import boto3

class Client(Client_Interface):


    def describe_security_groups(self) -> dict:
        self.aws_client = boto3.client('ec2')
        return self.aws_client.describe_security_groups()


    def describe_regions(self) -> dict:
        self.aws_client = boto3.client('ec2')
        return self.aws_client.describe_regions()


    def describe_db_instances(self) -> dict:
        self.aws_client = boto3.client('rds')
        return self.aws_client.describe_db_instances()

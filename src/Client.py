from src.Client_Interface import Client_Interface
import boto3

class Client(Client_Interface):

    def __init__(self):
        self.aws_client = boto3.client('ec2')


    def describe_security_groups(self) -> dict:
        return self.aws_client.describe_security_groups()


    def describe_regions(self) -> dict:
        return self.aws_client.describe_regions()

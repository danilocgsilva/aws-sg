import boto3
import os

class Client_Config:

    def set_region(self, region):
        os.environ['AWS_DEFAULT_REGION'] = region
        return self


    def set_profile(self, profile):
        os.environ['AWS_PROFILE'] = profile
        return self


    def get_client(self):
        ec2client = boto3.client('ec2')
        return ec2client

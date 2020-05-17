from src.Client import Client
import os

class Client_Config:

    def set_region(self, region):
        os.environ['AWS_DEFAULT_REGION'] = region
        return self


    def set_profile(self, profile):
        os.environ['AWS_PROFILE'] = profile
        return self


    def get_client(self):
        return Client()

from src.Client import Client
from src.Client_Config_Interface import Client_Config_Interface
import os

class Client_Config(Client_Config_Interface):

    def set_region(self, region: str):
        os.environ['AWS_DEFAULT_REGION'] = region
        return self


    def set_profile(self, profile):
        os.environ['AWS_PROFILE'] = profile
        return self


    def get_client(self):
        return Client()

from awssg.Client_Config_Interface import Client_Config_Interface
from awssg.Client_Interface import Client_Interface
from tests.Client_Mock import Client_Mock

class Client_Config_Mock(Client_Config_Interface):

    def set_region(self, region: str):
        self.region = region
        return self


    def set_profile(self, profile: str):
        self.profile = profile
        return self


    def get_client(self) -> Client_Interface:
        return Client_Mock()
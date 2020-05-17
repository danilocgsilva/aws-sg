from src.Client_Interface import Client_Interface
from tests.Data_Mocks import Data_Mocks
import json

class Client_Mock(Client_Interface):

    def describe_security_groups(self):
        data_mocks = Data_Mocks()
        data_string = data_mocks.get_sample_string_response()
        data = json.loads(data_string)
        return data

    def describe_regions(self):
        data_mocks = Data_Mocks()
        data_string = data_mocks.get_regions_string_mocked_data()
        data = json.loads(data_string)
        return data


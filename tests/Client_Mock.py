from awssg.Client_Interface import Client_Interface
from tests.Data_Mocks import Data_Mocks
import json

class Client_Mock(Client_Interface):

    def __init__(self):
        self.multiple_vpcs = False
    
    def setMultipleVpcs(self):
        self.multiple_vpcs = True
        return self

    def describe_security_groups(self) -> dict:
        data_string = Data_Mocks().get_sample_string_response()
        data = json.loads(data_string)
        return data

    def describe_regions(self) -> dict:
        data_string = Data_Mocks().get_regions_string_mocked_data()
        data = json.loads(data_string)
        return data

    def describe_db_instances(self) -> dict:
        data_string = Data_Mocks().get_rds_request_string_mocked_data()
        data = json.loads(data_string)
        return data

    def describe_specific_security_group(self, security_group_name: str) -> dict:
        data_string = Data_Mocks().get_json_string_filtered_sgs(security_group_name)
        data = json.loads(data_string)
        return data

    def describe_specific_security_group_by_id(self, security_group_id: str) -> dict:
        data_string = Data_Mocks().get_json_string_filtered_sgs_by_id(security_group_id)
        data = json.loads(data_string)
        return data

    def describe_vpcs(self) -> dict:
        if self.multiple_vpcs:
            data_string = Data_Mocks().get_multiple_vpcs_response()
        else: 
            data_string = Data_Mocks().get_json_vpcs_string()
        data = json.loads(data_string)
        return data

    def create_security_group(self, group_name: str, vpc_id):
        data_string = Data_Mocks().get_string_response_after_security_group_creation()
        data = json.loads(data_string)
        return data
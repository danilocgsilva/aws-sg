from awssg.Client import Client


class SG_Client:

    def __init__(self):
        self.client = None
        self.group_name = None
        self.vpc_id = None
        self.groupId = None

    def set_group_name(self, group_name):
        self.group_name = group_name
        return self

    def set_group_id(self, group_id: str):
        self.groupId = group_id
        return self

    def set_client(self, client: Client):
        self.client = client
        return self

    def validate_group_name(self):
        if self.group_name is None:
            raise Exception("You have not setted in group name to this class.")

    def validate_vpcs_count(self, vpcs_containers: dict):
        if len(vpcs_containers) != 1:
            raise Exception("You have no or more than a single virtual private cloud in this account, and now this program does not support such situation...")

    def prepare_before_aws(self):
        vpcs_response = self.client.describe_vpcs()
        vpcs_containers = vpcs_response.get('Vpcs', [{}])
        self.validate_vpcs_count(vpcs_containers)
        self.vpc_id = vpcs_containers[0].get('VpcId', '')

    def create_sg(self):
        self.validate_group_name()
        self.prepare_before_aws()
        result_creation = self.client.create_security_group(self.group_name, self.vpc_id)
        self.groupId = result_creation["GroupId"]
        return result_creation

    def delete_sg(self):
        self.prepare_before_aws()

        if self.group_name:
            self.client.delete_security_group_by_name(self.group_name)
            data_to_inform = self.group_name
        elif self.groupId:
            self.client.delete_security_group_by_id(self.groupId)
            data_to_inform = self.groupId
        else:
            raise Exception('Tries to delete a group without information about name or id.')

        print("Security group " + data_to_inform + " has been deleted.")

    def set_rule(self, group_id: str, protocol: str, ip: str, port: str):
        self.prepare_before_aws()
        self.client.set_rule(group_id, protocol, ip, port)

    def getGroupId(self) -> str:
        return self.groupId

    def getGroupName(self) -> str:
        return self.group_name

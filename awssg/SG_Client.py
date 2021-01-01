from awssg.Client import Client
import botocore

class SG_Client:

    def __init__(self):
        self.client = None
        self.group_name = None
        self.vpc_id = None
        self.groupId = None
        self.vpcs_containers = []

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

    # def validate_vpcs_count(self, vpcs_containers: dict):
    #     if len(vpcs_containers) != 1:
    #         raise Exception("You have no or more than a single virtual private cloud in this account, and now this program does not support such situation...")

    def prepare_before_aws(self, vpc = None):
        vpcs_response = self.client.describe_vpcs()
        self.vpcs_containers = vpcs_response.get('Vpcs', [{}])
        self.vpc_id = self.__chooseVpc(vpc)

    def create_default_sg(self, vpc = None):
        self.validate_group_name()
        self.prepare_before_aws(vpc)
        result_creation = self.client.create_security_group(self.group_name, self.vpc_id)
        self.groupId = result_creation["GroupId"]
        return result_creation

    def delete_sg(self):
        self.prepare_before_aws()

        if self.group_name:
            self.try_delete_by_name_or_warn(self.group_name)
        elif self.groupId:
            self.try_delete_by_id_or_warn(self.groupId)
        else:
            raise Exception('Tries to delete a group without information about name or id.')
    
    def try_delete_by_id_or_warn(self, group_id):
        try:
            self.client.delete_security_group_by_id(self.groupId)
            print("Security group with id " + group_id + " has been deleted.")
        except botocore.exceptions.ClientError as e:
            if e.response["Error"]["Code"] == "InvalidGroup.NotFound":
                print("The security group with id " + group_id + " does not exists!!!")
            else:
                raise e

    def try_delete_by_name_or_warn(self, gruoup_name):
        try:
            self.client.delete_security_group_by_name(gruoup_name)
            print("Security group with name " + gruoup_name + " has been deleted.")
        except botocore.exceptions.ClientError as e:
            if e.response["Error"]["Code"] == "InvalidGroup.NotFound":
                print("Security group with name " + gruoup_name + " does not exists!!!")
            else:
                raise e

    def set_rule(self, group_id: str, protocol: str, ip: str, port: str):
        self.prepare_before_aws()
        self.client.set_rule(group_id, protocol, ip, port)

    def getGroupId(self) -> str:
        return self.groupId

    def getGroupName(self) -> str:
        return self.group_name

    def getVpc(self):
        return self.vpc_id

    def __chooseVpc(self, vpc = None):
        if vpc == None and len(self.vpcs_containers) == 1:
            return self.vpcs_containers[0].get('VpcId', '')
        else:
            for vpcContainer in self.vpcs_containers:
                if vpcContainer.get('VpcId', '') == vpc:
                    return vpcContainer.get('VpcId', '')
            raise Exception("An invalid vpc has given.")

    def is_multiples_vpcs(self) -> bool:
        # print(self.vpcs_containers)
        return len(self.vpcs_containers) > 1

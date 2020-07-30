class SG_Client:

    def __init__(self):
        self.group_name = None


    def set_group_name(self, group_name):
        self.group_name = group_name
        return self


    def set_client(self, client):
        self.client = client
        return self


    def create_sg(self):

        if self.group_name == None:
            raise Exception("You have not setted in group name to this class.")

        vpcs_response = self.client.describe_vpcs()
        vpcs_containers = vpcs_response.get('Vpcs', [{}])

        if len(vpcs_containers) != 1:
            raise Exception("You have no or more than a single virtual private cloud in this account, and now this program does not support such situation...")

        vpc_id = vpcs_containers[0].get('VpcId', '')
        self.client.create_security_group(
            GroupName=self.group_name, 
            Description=self.group_name, 
            VpcId=vpc_id
        )
        print("Security group " + self.group_name + " has been just created in " + self.client.meta.region_name + ".")
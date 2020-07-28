import json

class RDS:

    def set_data(self, data: dict):
        self.data = data


    def set_string_data(self, string_data: str):
        self.data = json.loads(string_data)
        return self


    def get_name(self) -> str:
        return self.data["DBInstanceIdentifier"]


    def get_securities_groups_names(self) -> list:

        rds_sg_list = []

        for sg_data in self.data["VpcSecurityGroups"]:
            rds_sg_list.append(sg_data["VpcSecurityGroupId"]) 

        return rds_sg_list

from awssg.Client import Client

class Fetcher:

    def set_client(self, client: Client):
        self.client = client
        return self


    def get_sgs_data(self) -> dict:
        return self.client.describe_security_groups()


    def get_sgs_data_by_name(self, name: str) -> dict:
        return self.client.describe_specific_security_group(name)


    def get_all_regions_data(self) -> dict:
        return self.client.describe_regions()


    def get_rds_data(self, rds: str) -> dict:
        return self.client.describe_db_instances()

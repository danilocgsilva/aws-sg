from src.Client import Client

class Fetcher:

    def set_client(self, client: Client):
        self.client = client


    def sgs_data(self) -> dict:
        return self.client.describe_security_groups()


    def get_all_regions_data(self) -> dict:
        return 'ok'
        # return self.client.describe_security_groups()

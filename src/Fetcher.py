class Fetcher:

    def set_client(self, client):
        self.client = client


    def sgs_data(self):
        return self.client.describe_security_groups()



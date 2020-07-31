import json

class Ip_Permission:

    def set_data(self, data: dict):
        self.data = data
        return self

    def set_string_data(self, string_data: str):
        self.data = json.loads(string_data)
        return self

    def get_protocol(self) -> str:
        return self.data["IpProtocol"]

    def get_port(self) -> int:
        return self.data["FromPort"]

    def get_ip(self):
        return self.data["IpRanges"][0]["CidrIp"]

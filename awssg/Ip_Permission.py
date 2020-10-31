import json

class Ip_Permission:

    def set_data(self, data: dict):
        self.data = data
        return self

    def set_string_data(self, string_data: str):
        self.data = json.loads(string_data)
        return self

    def get_protocol(self) -> str:
        protocol = self.data["IpProtocol"]
        if protocol == "-1":
            return "anything"
        else:
            return protocol

    def get_port(self):
        if "FromPort" in self.data:
            return str(self.data["FromPort"])
        else:
            return ""

    def get_ip(self):
        if len(self.data["IpRanges"]) == 0:
            return "all"
        else:
            return self.data["IpRanges"][0]["CidrIp"]

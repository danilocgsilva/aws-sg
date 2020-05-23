import json

class SG:

    def set_string_data(self, string_data: str):
        self.data = json.loads(string_data)


    def set_data(self, data: dict):
        self.data = data


    def get_name(self) -> str:
        return self.data["GroupName"]


    def get_description(self) -> str:
        return self.data["Description"]




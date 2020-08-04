from awssg.SG import SG

class Printer:

    def __init__(self):
        self.sg = None
        self.name = False
        self.rules_count = False

    def set_sg(self, sg: SG):
        self.sg = sg
        return self

    def set_fields(self, fields_string=None):

        if None == fields_string:
            return self

        each_fields = fields_string.split(",")
        if 'name' in each_fields:
            self.name = True
        if 'rulescount' in each_fields:
            self.rules_count = True
        return self

    def get_string(self) -> str:
        return_string = self.sg.get_id()
        if self.name:
            return_string += "\n * Name: " + self.sg.get_name()
        if self.rules_count:
            return_string += "\n * Rules count: " + str(self.sg.get_rules_count())
        return return_string

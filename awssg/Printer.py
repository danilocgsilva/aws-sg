from awssg.SG import SG

class Printer:

    def __init__(self):
        self.sg = None
        self.name = False
        self.rules_count = False
        self.valid_fields = ['name', 'rulescount']
        self.fields_validated = None

    def set_sg(self, sg: SG):
        self.sg = sg
        return self

    def set_fields(self, fields_string=None):

        if None == fields_string:
            return self

        each_fields = fields_string.split(",")
        if self.valid_fields[0] in each_fields:
            self.name = True
        if self.valid_fields[1] in each_fields:
            self.rules_count = True
        return self

    def get_string(self) -> str:
        return_string = self.sg.get_id()
        if self.name:
            return_string += "\n * Name: " + self.sg.get_name()
        if self.rules_count:
            return_string += "\n * Rules count: " + str(self.sg.get_rules_count())
        return return_string

    def is_fields_valids(self) -> bool:
        return self.fields_validated

    def validate_fields(self, fields_string=None):
        if fields_string is not None:
            each_fields = fields_string.split(",")
            for provided_filter in each_fields:
                if not provided_filter in self.valid_fields:
                    self.fields_validated = False
                    break
            if self.fields_validated is None:
                self.fields_validated = True
        else:
            self.fields_validated = True

    def get_invalid_fields_message(self) -> str:
        exception_message = "There are invalid options in the fields options."
        exception_message += "\nValid options are:"
        for valid_option in self.valid_fields:
            exception_message += "\n" + valid_option
        return exception_message

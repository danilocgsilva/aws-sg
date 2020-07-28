import abc

class Parser_Interface(abc.ABC):

    @abc.abstractmethod
    def set_string_data(self, data_string: str):
        pass

    @abc.abstractmethod
    def set_data(self, data: dict):
        pass

    @abc.abstractclassmethod
    def get_list(self):
        pass

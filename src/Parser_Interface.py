import abc

class Parser_Interface(abc.ABC):

    @abc.abstractmethod
    def set_data(self, data: dict):
        pass

    @abc.abstractclassmethod
    def list(self):
        pass

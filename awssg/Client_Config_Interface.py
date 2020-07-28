import abc

class Client_Config_Interface(abc.ABC):

    @abc.abstractmethod
    def set_region(self, region: str):
        pass

    @abc.abstractmethod
    def set_profile(self, profile: str):
        pass

    @abc.abstractmethod
    def get_client(self):
        pass
import abc

class Client_Interface(abc.ABC):

    @abc.abstractmethod
    def describe_security_groups(self) -> dict:
        pass

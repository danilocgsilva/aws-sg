import abc

class Client_Interface(abc.ABC):

    @abc.abstractmethod
    def describe_security_groups(self) -> dict:
        pass

    @abc.abstractmethod
    def describe_regions(self) -> dict:
        pass

    @abc.abstractmethod
    def describe_db_instances(self) -> dict:
        pass

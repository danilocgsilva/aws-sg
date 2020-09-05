class SGConfig:

    def __init__(self, ip: str, protocol: str, port: int, name: str):
        self.ip = ip
        self.protocol = protocol
        self.port = port
        self.name = name

    def getIp(self) -> str:
        return self.ip

    def getProtocol(self) -> str:
        return self.protocol

    def getPort(self) -> int:
        return self.port

    def getName(self) -> str:
        return self.name

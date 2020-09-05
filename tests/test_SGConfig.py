import unittest
import sys
sys.path.insert(1, "..")
from awssg.SGConfig import SGConfig


class test_SGConfig(unittest.TestCase):

    def setUp(self):

        self.expected_ip = '123.456.789.012'
        self.expected_protocol = 'tcp'
        self.expected_port = 1234
        self.expected_name = 'MySecurityGroup'

        self.sGConfig = SGConfig(
            self.expected_ip,
            self.expected_protocol,
            self.expected_port,
            self.expected_name
        )

    def test_getIp(self):
        self.assertEqual(
            self.expected_ip,
            self.sGConfig.getIp()
        )

    def test_getProtocol(self):
        self.assertEqual(
            self.expected_protocol,
            self.sGConfig.getProtocol()
        )

    def test_getPort(self):
        self.assertEqual(
            self.expected_port,
            self.sGConfig.getPort()
        )

    def test_getName(self):
        self.assertEqual(
            self.expected_name,
            self.sGConfig.getName()
        )

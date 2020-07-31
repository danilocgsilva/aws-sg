import unittest
from tests.Data_Mocks import Data_Mocks
from awssg.Ip_Permission import Ip_Permission

class test_Ip_Permission(unittest.TestCase):

    def setUp(self):
        self.ip_permission = Ip_Permission()
        self.data_mocks = Data_Mocks()
        string_rule = self.data_mocks.get_string_single_ip_permission()
        self.ip_permission.set_string_data(string_rule)

    def test_get_port(self):
        expected_result = 22
        self.assertEqual(expected_result, self.ip_permission.get_port())

    def test_get_protocol(self):
        expected_result = "tcp"
        self.assertEqual(expected_result, self.ip_permission.get_protocol())

    def test_get_ip(self):
        expected_result = "210.64.32.200/32"
        self.assertEqual(expected_result, self.ip_permission.get_ip())





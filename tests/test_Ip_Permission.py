import unittest
from tests.Data_Mocks import Data_Mocks
from src.Ip_Permission import Ip_Permission

class test_Ip_Permission(unittest.TestCase):

    def setUp(self):
        self.ip_permission = Ip_Permission()
        self.data_mocks = Data_Mocks()


    def test_get_port(self):
        string_rule = self.data_mocks.get_string_single_ip_permission()
        self.ip_permission.set_string_data(string_rule)
        expected_result = 22
        self.assertEqual(expected_result, self.ip_permission.get_port())


    def test_get_protocol(self):
        string_rule = self.data_mocks.get_string_single_ip_permission()
        self.ip_permission.set_string_data(string_rule)
        expected_result = "tcp"
        self.assertEqual(expected_result, self.ip_permission.get_protocol())


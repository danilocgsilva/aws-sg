import unittest
import sys
sys.path.insert(1, '..')
from awssg.SG import SG
from awssg.Ip_Permission import Ip_Permission
from tests.Data_Mocks import Data_Mocks

class test_SG(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_SG, self).__init__(*args, **kwargs)
        self.sg = SG()

        self.sg.set_string_data(
            Data_Mocks().get_single_security_group_string_data()
        )

    def test_get_security_group_name(self):
        self.assertEqual("my-first-sg", self.sg.get_name())

    def test_get_security_group_description(self):
        self.assertEqual("Access from the backery", self.sg.get_description())

    def test_get_rules_type(self):
        self.assertTrue(isinstance(self.sg.get_rules(), list))

    def test_get_rules_count(self):
        rules_list = self.sg.get_rules()
        expected_rules_count = 1
        self.assertEqual(expected_rules_count, len(rules_list))

    def test_single_type_rule(self):
        rules_list = self.sg.get_rules()
        first_rule = rules_list[0]
        self.assertTrue(isinstance(first_rule, Ip_Permission))

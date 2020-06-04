import unittest
import sys
sys.path.insert(1, '..')
from src.SG import SG
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




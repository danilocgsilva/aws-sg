import unittest
import sys
sys.path.insert(1, '..')
from src.SG import SG
from tests.Data_Mocks import Data_Mocks

class test_SG(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_SG, self).__init__(*args, **kwargs)
        self.sg = SG()

        self.data_mocks = Data_Mocks()


    def test_get_security_group_name(self):

        self.sg.set_string_data(
            self.data_mocks.get_single_security_group_string_data()
        )

        self.assertEqual("my-first-sg", self.sg.get_name())


    def test_get_security_group_description(self):

        self.sg.set_string_data(
            self.data_mocks.get_single_security_group_string_data()
        )

        self.assertEqual("Access from the backery", self.sg.get_description())

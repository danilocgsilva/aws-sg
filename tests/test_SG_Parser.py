import unittest
import sys
sys.path.insert(1, '..')
from src.SG_Parser import SG_Parser
from tests.Data_Mocks import Data_Mocks

class test_SG(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_SG, self).__init__(*args, **kwargs)
        self.sg_parser = SG_Parser()

        data_mocks = Data_Mocks()

        sample_json_data = data_mocks.get_sample_string_response()
        self.sg_parser.set_string_data(sample_json_data)


    def test_correct_count_sg(self):
        security_groups_returned = self.sg_parser.list()
        self.assertEqual(3, len(security_groups_returned))


    def test_return_list(self):
        security_groups_returned = self.sg_parser.list()
        self.assertTrue(isinstance(security_groups_returned, list))


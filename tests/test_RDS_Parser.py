import unittest
from awssg.RDS_Parser import RDS_Parser
from awssg.RDS import RDS
from tests.Data_Mocks import Data_Mocks
from tests.Client_Mock import Client_Mock

class test_RDS_Parser(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_RDS_Parser, self).__init__(*args, **kwargs)
        self.client = Client_Mock()
        self.rds_parser = RDS_Parser()
        rds_data = self.client.describe_db_instances()
        self.rds_parser.set_data(rds_data)

    def test_correct_type(self):
        rds_lists = self.rds_parser.get_list()
        self.assertTrue(isinstance(rds_lists, list))

    def test_correct_rds_length(self):
        rds_lists = self.rds_parser.get_list()
        self.assertEqual(1, len(rds_lists))

    def test_is_element_exists(self):
        existing_element = "myinstance"
        existing_return = self.rds_parser.is_element_exists(existing_element)
        self.assertTrue(existing_return)

    def test_get_correct_first_occurrence_type(self):
        rds_list = self.rds_parser.get_list()
        first_element = rds_list[0]
        self.assertTrue(isinstance(first_element, RDS))


    def test_get_correct_name_first_element(self):
        rds_list = self.rds_parser.get_list()
        first_element = rds_list[0]
        first_element_name = first_element.get_name()
        expected_name = "myinstance"
        self.assertEqual(expected_name, first_element_name)


    def test_get_rds_by_name_correct_instance_type(self):
        rds_returned = self.rds_parser.get_rds_by_name("myinstance")
        self.assertTrue(isinstance(rds_returned, RDS))


    def test_get_rds_by_name_correct_matching_name(self):
        expected_name = "myinstance"
        rds_returned = self.rds_parser.get_rds_by_name(expected_name)
        self.assertEqual(expected_name, rds_returned.get_name())

if __name__ == '__main__':
    unittest.main()
    
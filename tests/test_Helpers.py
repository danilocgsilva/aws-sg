import unittest
from awssg.Helpers import get_regions, readable_single_region_data
from tests.Client_Mock import Client_Mock
from tests.Client_Config_Mock import Client_Config_Mock

class test_Helpers(unittest.TestCase):

    def test_regions_list_correct_type(self):
        client = Client_Mock()
        regions = get_regions(client)
        self.assertTrue(isinstance(regions, list))


    def test_correct_data_fetched_for_regions_list(self):
        client = Client_Mock()
        regions = get_regions(client)
        expected_list = ["sa-north-1", "ju-south-1", "mo-west-3"]
        self.assertListEqual(expected_list, regions)


    def test_readable_single_region_data(self):
        region = 'us-east-1'

        expected_return = "\nmy-first-sg\nAny other place\ncrazy-hash-from-elastic-beanstalk"
        string_returned = readable_single_region_data(region, Client_Config_Mock())

        self.assertEqual(expected_return, string_returned)

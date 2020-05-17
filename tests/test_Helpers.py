import unittest
from src.Helpers import get_regions
from tests.Client_Mock import Client_Mock

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

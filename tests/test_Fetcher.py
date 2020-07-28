import unittest
from awssg.Fetcher import Fetcher
from tests.Client_Mock import Client_Mock

class test_Fetcher(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_Fetcher, self).__init__(*args, **kwargs)
        self.fetcher = Fetcher()

    
    def test_fetch_request_right_format(self):
        client = Client_Mock()
        self.fetcher.set_client(client)
        result_fetched = self.fetcher.get_sgs_data()
        self.assertTrue(isinstance(result_fetched, dict))


    def test_fetch_request_right_format_for_regions(self):
        self.fetcher.set_client(Client_Mock())
        result_fetched = self.fetcher.get_all_regions_data()
        self.assertTrue(isinstance(result_fetched, dict))


    def test_get_sgs_data_by_name(self):
        self.fetcher.set_client(Client_Mock())
        result_fetched = self.fetcher.get_sgs_data_by_name("allow-http")
        self.assertTrue(isinstance(result_fetched, dict))


    def test_get_sgs_data_by_non_existing_name(self):
        self.fetcher.set_client(Client_Mock())
        with self.assertRaises(Exception):
            self.fetcher.get_sgs_data_by_name("non existent")



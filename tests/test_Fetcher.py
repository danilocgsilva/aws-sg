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
        sg_name = "allow-http"
        result_fetched = self.fetcher.get_sgs_data_by_name(sg_name)
        self.assertTrue(isinstance(result_fetched, dict))

    def test_get_sgs_data_by_non_existing_name(self):
        self.fetcher.set_client(Client_Mock())
        with self.assertRaises(Exception):
            self.fetcher.get_sgs_data_by_name("non existent")

    def test_get_sgs_data_by_id(self):
        self.fetcher.set_client(Client_Mock())
        sg_id = "sg-092498379087908"
        result_fetched = self.fetcher.get_sgs_data_by_id(sg_id)
        self.assertTrue(isinstance(result_fetched, dict))


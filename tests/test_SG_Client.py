import unittest
import sys
sys.path.insert(1, "..")
from awssg.SG_Client import SG_Client
from tests.Client_Mock import Client_Mock


class test_SG_Client(unittest.TestCase):

    def setUp(self):
        self.sg_client = SG_Client()

    def test_set_client_fluent_interface(self):
        object = self.sg_client.set_client("something")
        self.assertTrue(isinstance(object, SG_Client))

    def test_exception_multiples_vpcs_create_sg(self):
        client = Client_Mock()
        self.sg_client.set_client(client).set_group_name("stub_name")
        with self.assertRaises(Exception):
            self.sg_client.create_sg()

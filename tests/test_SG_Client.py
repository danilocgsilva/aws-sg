import unittest
import sys
sys.path.insert(1, "..")
from awssg.SG_Client import SG_Client

class test_SG_Client(unittest.TestCase):

    def setUp(self):
        self.sg_client = SG_Client()


    def test_set_client_fluent_interface(self):
        object = self.sg_client.set_client("something")
        self.assertTrue(isinstance(object, SG_Client))


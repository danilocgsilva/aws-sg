import unittest
import sys
sys.path.insert(1, '..')
from awssg.Fetcher import Fetcher
from awssg.SG_Parser import SG_Parser
from awssg.RDS_Parser import RDS_Parser
from tests.Client_Mock import Client_Mock

class test_SG(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_SG, self).__init__(*args, **kwargs)
        self.sg_parser = SG_Parser()

        client = Client_Mock()
        sg_data = client.describe_security_groups()
        self.sg_parser.set_data(sg_data)

    def test_correct_count_sg(self):
        security_groups_returned = self.sg_parser.get_list()
        self.assertEqual(3, len(security_groups_returned))

    def test_return_list(self):
        security_groups_returned = self.sg_parser.get_list()
        self.assertTrue(isinstance(security_groups_returned, list))

    def test_is_rds_instance_name_exists_true(self):
        client = Client_Mock()
        rds_data = client.describe_db_instances()

        rds_parser = RDS_Parser()
        rds_parser.set_data(rds_data)

        rds_name = "myinstance"

        exists = self.sg_parser.is_rds_instance_name_exists(rds_name, client)

        self.assertTrue(exists)

    def test_is_rds_instance_name_exists_false(self):
        client = Client_Mock()
        rds_data = client.describe_db_instances()

        rds_parser = RDS_Parser()
        rds_parser.set_data(rds_data)

        rds_name = "non_existent"

        exists = self.sg_parser.is_rds_instance_name_exists(rds_name, client)

        self.assertFalse(exists)

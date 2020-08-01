import unittest
import sys
sys.path.insert(1, '..')
from awssg.SG_Parser import SG_Parser
from awssg.RDS_Parser import RDS_Parser
from awssg.SG import SG
from tests.Client_Mock import Client_Mock

class test_SG(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_SG, self).__init__(*args, **kwargs)
        self.sg_parser = SG_Parser()

        self.client = Client_Mock()
        sg_data = self.client.describe_security_groups()
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

    def test_get_list_by_single_security_group_by_id(self):
        sg_id = "sg-092498379087908"
        new_sg_data = self.client.describe_specific_security_group_by_id(sg_id)
        self.sg_parser.set_data(new_sg_data)
        security_groups_returned = self.sg_parser.get_list()
        self.assertTrue(isinstance(security_groups_returned, list))

    def test_get_list_by_single_security_group_by_name(self):
        sg_name = "allow-http"
        new_sg_data = self.client.describe_specific_security_group(sg_name)
        self.sg_parser.set_data(new_sg_data)
        security_groups_returned = self.sg_parser.get_list()
        self.assertTrue(isinstance(security_groups_returned, list))

    def test_get_number_list_by_name(self):
        sg_name = "allow-http"
        new_sg_data = self.client.describe_specific_security_group(sg_name)
        self.sg_parser.set_data(new_sg_data)
        security_groups_returned = self.sg_parser.get_list()
        self.assertEqual(1, len(security_groups_returned))

    def test_get_sg(self):
        sg_name = "allow-http"
        new_sg_data = self.client.describe_specific_security_group(sg_name)
        self.sg_parser.set_data(new_sg_data)
        sg = self.sg_parser.get_sg()
        self.assertTrue(isinstance(sg, SG))

    def test_get_sg_if_multiple_sgs(self):
        with self.assertRaises(Exception):
            self.sg_parser.get_sg()


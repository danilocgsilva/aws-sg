import unittest
from tests.Data_Mocks import Data_Mocks
from awssg.RDS import RDS

class test_RDS(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_RDS, self).__init__(*args, **kwargs)
        self.rds = RDS().set_string_data(
            Data_Mocks().get_json_string_from_single_rds()
        )


    def test_get_name(self):
        expected_name = "myinstancename"
        rds_name_returned = self.rds.get_name()
        self.assertEqual(expected_name, rds_name_returned)


    def test_get_securities_groups_names_count(self):
        security_groups_count_expected = 2
        security_groups_returned = len(self.rds.get_securities_groups_names())
        self.assertEqual(security_groups_count_expected, security_groups_returned)


    def test_get_securities_groups_names_members(self):
        security_groups_names = self.rds.get_securities_groups_names()
        security_groups_names_expected = ["sg-asdkljhkjhasdf", "sg-asdlfkjahfsd"]
        self.assertListEqual(security_groups_names_expected, security_groups_names)

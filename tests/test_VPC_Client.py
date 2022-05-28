from awssg.VPC_Client import VPC_Client
from aws_api_mock.EC2_Client import EC2_Client
import unittest

class test_VPC_Client(unittest.TestCase):

    def setUp(self):
        self.vpc_client = VPC_Client(EC2_Client())

    def test_vpc_not_exists(self):
        vpc_id = 'abc1234'
        self.assertFalse(self.vpc_client.vpc_exists(vpc_id))

    def test_vpc_exists(self):
        vpc_id = 'vpc-fc6d63e7c67246b85'
        self.assertTrue(self.vpc_client.vpc_exists(vpc_id))

if __name__ == '__main__':
    unittest.main()

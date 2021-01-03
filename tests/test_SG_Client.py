import unittest
import sys
# from .Client_Mock import Client_Mock
sys.path.insert(1, "..")
from awssg.SG_Client import SG_Client
from tests.Client_Mock import Client_Mock
class test_SG_Client(unittest.TestCase):

    def setUp(self):
        self.sg_client = SG_Client()

    def test_set_client_fluent_interface(self):
        object = self.sg_client.set_client("something")
        self.assertTrue(isinstance(object, SG_Client))

    def test_exception_create_sg_missing_ip(self):
        protocol = 'tcp'
        port = '1234'
        sg_id = 'sg-123abcd'
        with self.assertRaises(Exception):
            self.sg_client.set_rule(sg_id, protocol, None, port)

    def test_set_group_name(self):
        test_name = 'my-sg-name'
        self.sg_client.set_client(Client_Mock()).set_group_name(test_name)
        self.assertEqual(test_name, self.sg_client.getGroupName())

    def test_vpcMultiplesGiven(self):
        clientBoto3 = Client_Mock().setMultipleVpcs()
        sg_test_name = 'my-sg-name'
        self.sg_client\
            .set_client(clientBoto3)\
            .set_group_name(sg_test_name)\
            .set_vpc("vpc-a30ff249b44e63bfe")
        self.sg_client.create_default_sg()
        expectedVpc = "vpc-a30ff249b44e63bfe"
        choosedVpc = self.sg_client.getVpc()
        self.assertEqual(expectedVpc, choosedVpc)

    def test_vpcMultiplesGivenInvalidOne(self):
        clientBoto3 = Client_Mock().setMultipleVpcs()
        sg_test_name = 'my-sg-name'
        self.sg_client.set_client(clientBoto3)
        self.sg_client.set_group_name(sg_test_name)
        self.sg_client.set_vpc("vpc-4919cd1632d1d03b6")
        with self.assertRaises(Exception):
            self.sg_client.create_default_sg()

    def test_getDefaultVpc(self):
        clientBoto3 = Client_Mock()
        sg_test_name = 'my-sg-name'
        self.sg_client.set_client(clientBoto3).set_group_name(sg_test_name)
        self.sg_client.create_default_sg()
        expectedVpc = "vpc-abcd1234"
        choosedVpc = self.sg_client.getVpc()
        self.assertEqual(expectedVpc, choosedVpc)

    def test_setNoVpcWithMultiplesVpcs(self):
        clientBoto3 = Client_Mock().setMultipleVpcs()
        sg_test_name = 'my-sg-name'
        self.sg_client.set_client(clientBoto3)
        self.sg_client.set_group_name(sg_test_name)
        with self.assertRaises(Exception):
            self.sg_client.create_default_sg()

    def test_checkVpcAmountsMultiples(self):
        clientBoto3 = Client_Mock().setMultipleVpcs()
        sg_test_name = 'my-sg-name'
        self.sg_client.set_client(clientBoto3).\
            set_group_name(sg_test_name)
        self.assertTrue(self.sg_client.is_multiples_vpcs())

    def test_checkVpcAmountsSingle(self):
        clientBoto3 = Client_Mock()
        sg_test_name = 'my-sg-name'
        self.sg_client.set_client(clientBoto3).\
            set_group_name(sg_test_name)
        self.assertFalse(self.sg_client.is_multiples_vpcs())

if __name__ == '__main__':
    unittest.main()

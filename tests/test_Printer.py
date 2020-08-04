import unittest
import sys
sys.path.insert(1, "..")
from awssg.Printer import Printer
from awssg.SG import SG
from tests.Data_Mocks import Data_Mocks


class test_Printer(unittest.TestCase):

    def setUp(self) -> None:
        self.printer = Printer()
        self.sg = SG()

        self.sg.set_string_data(
            Data_Mocks().get_single_security_group_string_data()
        )

    def test_print_only_sgid(self):
        sgidreturn = "sg-2f31fa12094"
        self.printer.set_sg(self.sg)
        returned_string = self.printer.get_string()
        self.assertEqual(returned_string, sgidreturn)

    def test_print_with_name(self):
        sgidreturn = "sg-2f31fa12094"
        sgidreturn += "\n * Name: my-first-sg"
        self.printer.set_sg(self.sg).set_fields("name")
        returned_string = self.printer.get_string()
        self.assertEqual(returned_string, sgidreturn)

    def test_print_with_rulescount(self):
        sgidreturn = "sg-2f31fa12094"
        sgidreturn += "\n * Rules count: 1"
        self.printer.set_sg(self.sg).set_fields("rulescount")
        returned_string = self.printer.get_string()
        self.assertEqual(returned_string, sgidreturn)

    def test_print_with_rulescount_and_name(self):
        sgidreturn = "sg-2f31fa12094"
        sgidreturn += "\n * Name: my-first-sg"
        sgidreturn += "\n * Rules count: 1"
        self.printer.set_sg(self.sg).set_fields("name,rulescount")
        returned_string = self.printer.get_string()
        self.assertEqual(returned_string, sgidreturn)
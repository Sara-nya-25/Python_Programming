# TDD -Unit testing for Bank program
import unittest
from .class_3_Bank import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        # Create a fresh account for every test
        self.acc = BankAccount(acc_holder='Sara',initial_balance=1000, interest_rate=0.01)

    def test_deposit(self):
        self.acc.deposit(500)
        self.assertEqual(self.acc.get_balance(), 1500)

    def test_withdraw(self):
        self.acc.withdraw(300)
        self.assertEqual(self.acc.get_balance(), 700)

    def test_apply_interest(self):
        # 5% of 100 is 5. Total should be 105.
        self.acc.apply_interest()
        self.assertEqual(self.acc.get_balance(), 1010)

    def test_can_afford(self):
        self.assertTrue(self.acc.can_afford(800))
        self.assertFalse(self.acc.can_afford(1200))

    def test_history_logging(self):
        # Initial history + 1 deposit = 2 entries
        self.acc.deposit(50)
        # We access the private attribute for testing purposes using name mangling
        history_count = len(self.acc._BankAccount__history)
        self.assertEqual(history_count, 2)

"""
Test results:
LAB_6/class_3_Bank_test.py::TestBankAccount::test_apply_interest PASSED                                                                                                      [ 20%]
LAB_6/class_3_Bank_test.py::TestBankAccount::test_can_afford PASSED                                                                                                          [ 40%]
LAB_6/class_3_Bank_test.py::TestBankAccount::test_deposit PASSED                                                                                                             [ 60%]
LAB_6/class_3_Bank_test.py::TestBankAccount::test_history_logging PASSED                                                                                                     [ 80%]
LAB_6/class_3_Bank_test.py::TestBankAccount::test_withdraw PASSED                                                                                                            [100%]

"""
"""
Create a class that represents a bank account. The bank should be able to:
deposit money (deposit)
withdraw money (withdraw)
return the current balance (balance)
calculate interest (apply_interest, adds the interest to the account)
tell if you can afford to pay a bill (return True/False)

Make a method for each function.

Write unit tests for each function. Feel free to use the TDD method, starting with the test cases before writing the code.
"""
import datetime

class BankAccount:
    def __init__(self, acc_holder, initial_balance=0.0, interest_rate=0.01):
        self.__customer = acc_holder
        self.__balance = float(initial_balance)
        self.__interest_rate = float(interest_rate)
        # Initialize the history list with the opening deposit
        self.__history = [f"Account opened with ${initial_balance:,.2f}"]

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__history.append(f"Deposited: ${amount:,.2f}")
        return self.__balance

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__history.append(f"Withdrew: ${amount:,.2f} kr")
            return True
        else:
            self.__history.append(f"FAILED Withdrawal: ${amount:,.2f} kr (Insufficient funds)")
            return False

    def apply_interest(self):
        interest = self.__balance * self.__interest_rate
        self.__balance += interest
        self.__history.append(f"Interest Applied: ${interest:,.2f}% (@{self.__interest_rate*100}%)")

    def get_balance(self):
        return self.__balance

    def show_history(self):
        print(f"\n--- Transaction History for {self.__customer} ---")
        for entry in self.__history:
            print(f"  > {entry}")
        print(f"Current Balance: ${self.__balance:,.2f}\n")

    def can_afford(self, bill_amount):
        return self.__balance >= bill_amount
# Example usage:
my_acc = BankAccount("Sara", 1000)
my_acc.deposit(500)
my_acc.withdraw(200)
my_acc.apply_interest()
my_acc.withdraw(5000) # This will fail
my_acc.show_history()
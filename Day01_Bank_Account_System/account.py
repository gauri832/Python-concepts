# Generated from: account.ipynb
# Converted at: 2026-01-02T17:35:44.792Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

class Account:
    bank_name = "XYZ Bank"  # class attribute

    def __init__(self, owner_name, initial_balance=0):
        self.owner_name = owner_name
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        self.transaction_history.append(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        self.transaction_history.append(f"Withdrew ₹{amount}")

    def display_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    def show_transactions(self):
        print("Transaction History:")
        for txn in self.transaction_history:
            print("-", txn)

    def __str__(self):
        return f"{self.owner_name} | {Account.bank_name} | Balance: ₹{self.balance}"


account1 = Account("Gauri", 5000)

print(account1)

account1.deposit(1000)
account1.withdraw(2000)
account1.display_balance()
account1.show_transactions()


%%writefile account.py

class Account:
    bank_name = "XYZ Bank"

    def __init__(self, owner_name, initial_balance=0):
        self.owner_name = owner_name
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        self.transaction_history.append(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        self.transaction_history.append(f"Withdrew ₹{amount}")

    def display_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    def show_transactions(self):
        if not self.transaction_history:
            print("No transactions yet.")
            return
        print("Transaction History:")
        for txn in self.transaction_history:
            print("-", txn)

    def __str__(self):
        return f"{self.owner_name} | {Account.bank_name} | Balance: ₹{self.balance}"


!dir


%%writefile main.py

from account import Account

def main():
    account1 = Account("Gauri", 5000)

    print(account1)

    account1.deposit(1000)
    account1.withdraw(2000)
    account1.display_balance()
    account1.show_transactions()

if __name__ == "__main__":
    main()


!python main.py


import sys
sys.path.append('.')


import importlib
import account
importlib.reload(account)


!dir  # Windows
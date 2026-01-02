# Generated from: main.ipynb
# Converted at: 2026-01-02T17:36:44.446Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

from account import Account

account1 = Account("Gauri", 5000)

print(account1)

account1.deposit(1000)
account1.withdraw(2000)
account1.display_balance()
account1.show_transactions()
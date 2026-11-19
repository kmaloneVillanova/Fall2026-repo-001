from bank_account import BankAccount

account = BankAccount("1234", 100)
print(account)
account.deposit(50)
print(f'your balance is {account.get_balance()}')
account.withdraw(100)
print(account)
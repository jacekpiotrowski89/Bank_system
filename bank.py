class Transaction:
    def __init__(self, amount, transaction_type):
        self.amount = amount
        self.transaction_type = transaction_type


class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name 
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(Transaction(amount, 'Deposit'))
            print(f'Deposit of {amount}$ is successful. New balance: {self.balance}$')
        else:
            print('Invalid deposit amount.')
    
    def withdrawal(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction(amount, 'withdrawal'))
            print(f'Withdraw of {amount}$ is successful. New balance: {self.balance}$')
        else:
            print('Invalid withdrawal amount or insufficient funds.')

    def display_transaction(self):
        print('\nTransaction History: ')
        for transaction in self.transactions:
            print(f'{transaction.amount}$ {transaction.transaction_type}')

    def display_balance(self):
        print(f'Current balance for Account {self.account_number}: {self.balance}$')

class Bank: 
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, account_number, holder_name, initial_balance=0):
        if account_number not in self.accounts:
            new_account = Account(account_number, holder_name, initial_balance)
            self.accounts[account_number] = new_account
            print(f'Account created successfully for {holder_name}. Account number: {account_number}.') 
        else:
            print('Account with the given number already exist.')

    def get_account(self, account_number):
        return self.accounts.get(account_number)
    

bank = Bank('Azizi Bank')

# create account
alice_account = bank.create_account(10001, 'Alice', 1000)
bob_account = bank.create_account(10002, 'Bob')

# Accesing account

alice_account = bank.get_account(10001)
bob_account = bank.get_account(10002)

# making transactions

alice_account.deposit(500)
alice_account.withdrawal(1499)

bob_account.deposit(1000)
bob_account.withdrawal(500)

# displaying info

alice_account.display_transaction()
alice_account.display_balance()

bob_account.display_transaction()
bob_account.display_balance()


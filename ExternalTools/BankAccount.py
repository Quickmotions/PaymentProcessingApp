# Fergus Haak - 13/12/2022 - Payment Processing Application

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited to account.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

    def check_balance(self):
        print(f"Current balance: {self.balance}")


bank_accounts = [BankAccount("Fergus Haak", 1000),
                 BankAccount("James Finlay", 7000),
                 BankAccount("Paul Thomas", 12000)
                 ]


def authorize(name) -> BankAccount:
    for account in bank_accounts:
        if account.name == name:
            return account

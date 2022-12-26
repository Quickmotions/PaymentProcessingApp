# Fergus Haak - 13/12/2022 - Payment Processing Application
import asyncio
import random
import aiohttp
import asyncio


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.outstanding = []

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited to account.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

    def check_balance(self):
        print(f"Current balance: {self.balance}")


class OutStandingPayment:
    def __init__(self, card_name, amount):
        self.card_name = card_name;
        self.amount = amount
        self.id = random.randint(1000000, 9999999)


bank_accounts: list[BankAccount] = [
        BankAccount("Fergus Haak", 1000),
        BankAccount("James Finlay", 7000),
        BankAccount("Paul Thomas", 12000)
    ]

bank_captures: list[OutStandingPayment] = []


def authorize(name) -> BankAccount:
    for account in bank_accounts:
        if account.name == name:
            return account


def bank_capture(name, amount) -> int:
    for account in bank_accounts:
        if account.name == name:
            out_payment = OutStandingPayment(name, amount)
            bank_captures.append(out_payment)
            return out_payment.id


async def capture_payment():
    for capture in bank_captures:
        await asyncio.sleep(random.randint(1, 10))
        for account in bank_accounts:
            if account.name == capture.card_name:
                account.balance -= capture.amount

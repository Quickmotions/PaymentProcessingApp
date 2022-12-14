# Fergus Haak - 13/12/2022 - Payment Processing App
from PaymentSystems.PaymentStatus import PaymentStatus
from PaymentSystems.Authentication import Authentication
from ExternalTools.BankAccount import authorize, BankAccount


class Payment:
    def __init__(self, amount, status=None):
        self.amount = amount
        self.status = status or PaymentStatus()
        self.authentication = Authentication()


class CreditCardPayment(Payment):
    def __init__(self, amount, card_name, card_number, expiration_date):
        super().__init__(amount)
        self.card_name = card_name
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.bank = None

    def authenticate(self):
        account = authorize(self.card_name)
        if account is not None:
            self.status.complete()
            self.bank = account


class PayPalPayment(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email


class BitcoinPayment(Payment):
    def __init__(self, amount, address):
        super().__init__(amount)
        self.address = address

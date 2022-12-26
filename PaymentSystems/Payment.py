# Fergus Haak - 13/12/2022 - Payment Processing App
from PaymentSystems.PaymentStatus import PaymentStatus
from PaymentSystems.Authentication import Authentication
from PaymentSystems.ErrorHandler import AuthenticationError, CaptureError
from ExternalTools.BankAccount import authorize, bank_capture, BankAccount


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
        self.capture_id = None

    def authenticate(self):
        account = authorize(self.card_name)
        if account is not None:
            self.status.authorised()
            self.bank = account
            return
        raise AuthenticationError()

    def capture(self):
        """requests funds to be transferred from customer to merchant account"""
        capture_id = bank_capture(self.card_name, self.amount)
        if capture_id is not None:
            self.status.pending()
            self.capture_id = capture_id
            return
        raise CaptureError()


class PayPalPayment(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email


class BitcoinPayment(Payment):
    def __init__(self, amount, address):
        super().__init__(amount)
        self.address = address

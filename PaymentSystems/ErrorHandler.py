# Fergus Haak - 14/12/2022 - Payment Processing Application

from abc import ABC, abstractmethod


class PaymentError(Exception, ABC):
    def __init__(self):
        self.message = self.get_error_message()

    def __str__(self):
        return self.message

    @abstractmethod
    def get_error_code(self):
        pass

    @abstractmethod
    def get_error_message(self):
        pass


class InvalidCardError(PaymentError):
    def get_error_code(self):
        return 1001

    def get_error_message(self):
        return "Invalid card information"


class InsufficientFundsError(PaymentError):
    def get_error_code(self):
        return 1002

    def get_error_message(self):
        return "Insufficient funds"


class AuthenticationError(PaymentError):
    def get_error_code(self):
        return 1003

    def get_error_message(self):
        return "Authentication failed"


class CaptureError(PaymentError):
    def get_error_code(self):
        return 1004

    def get_error_message(self):
        return "Capture failed"

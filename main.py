# Fergus Haak - 13/12/2022 - Payment Processing App
from PaymentSystems.Payment import *


if __name__ == '__main__':
    payment = CreditCardPayment(100, "Fergus Haak", 2934234523421234, "23/12/23")
    print(payment.status.processed)
    payment.authenticate()
    print(payment.status.processed)

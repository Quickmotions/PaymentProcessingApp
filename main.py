# Fergus Haak - 13/12/2022 - Payment Processing App
from PaymentSystems.Payment import CreditCardPayment, PayPalPayment, BitcoinPayment

payments = []

if __name__ == '__main__':

    # payment comes through
    payment_1 = CreditCardPayment(100, "Fergus Haak", 2934234523421234, "23/12/23")
    payments.append(payment_1)
    # Authorization
    payment_1.authenticate()
    # capture Payment
    payment_1.capture()
    print(payment_1.capture_id)
    # await bank confirmation
    # TODO: create threads: bank capture processing cycle / await bank process finishing
    #  Use Async methods to await the processing of the bank capture



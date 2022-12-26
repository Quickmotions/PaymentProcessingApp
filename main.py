# Fergus Haak - 13/12/2022 - Payment Processing App
import asyncio
import random
import threading
from PaymentSystems.Payment import CreditCardPayment, PayPalPayment, BitcoinPayment
from ExternalTools.BankAccount import capture_payment

payments = []


def run_async_in_thread():
    asyncio.run(capture_payment())


if __name__ == '__main__':
    for _ in range(10):
        # payment comes through
        payment_1 = CreditCardPayment(random.randint(1, 99), "Fergus Haak", 2934234523421234, "23/12/23", "Nord")
        payments.append(payment_1)
        # Authorization
        payment_1.authenticate()
        # capture Payment
        payment_1.capture()
        # await bank confirmation
    threading.Thread(target=run_async_in_thread).start()
    print("done")
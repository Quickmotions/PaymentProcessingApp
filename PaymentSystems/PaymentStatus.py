# Fergus Haak - 13/12/2022 - Payment Processing Application

class PaymentStatus:
    def __init__(self, processed=False):
        self.processed = processed

    def complete(self):
        self.processed = True

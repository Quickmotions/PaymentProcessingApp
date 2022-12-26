# Fergus Haak - 13/12/2022 - Payment Processing Application

class PaymentStatus:
    def __init__(self, processed=False):
        self.processed = processed
        self.process = "Authorisation"

    def authorised(self):
        self.process = "Authorised"

    def pending(self):
        self.process = "Pending"

    def complete(self):
        self.process = "Complete"
        self.processed = True

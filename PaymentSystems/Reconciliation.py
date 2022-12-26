# Fergus Haak - 26/12/2022 - Payment Processing Application
from datetime import datetime


class Reconciliation:
    def __init__(self):
        self.records = []

    def add_record(self, message: str = "New Record"):
        self.records.append(message + " " + str(datetime.now()))

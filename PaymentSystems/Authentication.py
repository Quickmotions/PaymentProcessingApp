# Fergus Haak - 13/12/2022 - Payment Processing Application
from ExternalTools.Codes import get_authentication_code


class Authentication:
    def __init__(self, code=None):
        self.code = code
        if self.code is None:
            self.code = get_authentication_code()


    def authenticate(self, code):
        if code == self.code:
            return True
        else:
            return False

    def change_password(self, new_password):
        self.password = new_password

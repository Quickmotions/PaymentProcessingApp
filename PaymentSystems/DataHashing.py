# Fergus Haak - 14/12/2022 - Payment Processing Application
import hashlib


class Hash:
    def __init__(self, algorithm):
        # Store the specified hashing algorithm
        self.algorithm = hashlib.sha256
        self.hashes = []

    def save_hashes(self):
        ...

    def load_hashes(self):
        ...

    def check_hash(self):
        ...

    def hash_data(self, data):
        # Create a new instance of the specified hash algorithm
        hash_algorithm = self.algorithm()

        # Update the hash object with the data to be hashed
        hash_algorithm.update(data.encode('utf-8'))

        # Get the hexadecimal representation of the hash
        hex_digest = hash_algorithm.hexdigest()

        # Return the hash
        return hex_digest


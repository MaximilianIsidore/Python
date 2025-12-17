class HashTable:
    def __init__(self):
        # Initialize collection as an empty dictionary
        self.collection = {}

    def hash(self, string):
        # Sum Unicode values of characters in the string
        hash_value = 0
        for char in string:
            hash_value += ord(char)
        return hash_value

    def add(self, key, value):
        hashed_key = self.hash(key)

        # If hash does not exist, create a new nested dictionary
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}

        # Store the key-value pair in the nested dictionary
        self.collection[hashed_key][key] = value

    def remove(self, key):
        hashed_key = self.hash(key)

        # Check if hash and key exist before removing
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            del self.collection[hashed_key][key]

            # Optional cleanup: remove hash if empty
            if not self.collection[hashed_key]:
                del self.collection[hashed_key]

    def lookup(self, key):
        hashed_key = self.hash(key)

        # Return value if key exists, otherwise None
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            return self.collection[hashed_key][key]
        return None

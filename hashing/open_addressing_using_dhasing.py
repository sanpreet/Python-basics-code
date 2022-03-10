class open_addressing_using_dhashing:

    def __init__(self, table_size):
        self.table_size = table_size
        self.table = list(None for i in range(self.table_size))
        self.state = list(0 for i in range(self.table_size))

    def hash_1(self, key):
        """
        :param key: This is key inserted by the user to enter in the table
        :return: the index in the table to insert the key. To note is
        hash1 is significant when there is no collision for value to be inserted
        keep in mind that table size should be more or equal to number of keys to be
        inserted
        """
        return key % self.table_size

    def hash_2(self, key):
        """
        :param key:Key to be inserted by the user
        :return: if there is a collision occured when hash_1 is called, then combination of
        hash_1 and hash_2 is called to find the vacant index in the table to insert the key
        To find 100 % vacant index, it is important that hash_2 uses prime number and
        is less than size of table because in one ideal case one can fill the index using hash_1
        only. I will use table size = 8 to make prime number i.e 7
        """
        prime_number = self.table_size - 1
        return prime_number - (key % prime_number)

    def insert_key(self, key):
        index, count = self.hash_1(key=key), 1
        hash_two = self.hash_2(key)
        while self.state[index] == 1:
            """
            this means that such index in the table is already occupied
            hence we need to call combination of hash1 and hash 2
            """
            index = (index + count * hash_two) % self.table_size
            count += 1

        self.table[index], self.state[index] = key, 1


double_hash_object = open_addressing_using_dhashing(8)
double_hash_object.insert_key(4)
double_hash_object.insert_key(12)
# double_hash_object.insert_key(20)
# double_hash_object.insert_key(28)
print("table is created...", double_hash_object.table)
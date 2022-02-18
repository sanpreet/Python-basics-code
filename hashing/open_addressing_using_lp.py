class open_addressing_lp:

    def __init__(self, table_size):
        self.table_size = table_size
        self.table = [None] * self.table_size

    def linear_hash_function(self, value):
        """
        Numbers of values is always less than or equal to table size
        load factor can be 1 as number of values are equal to table size
        :return: index where to insert the value always an empty index to insert the value
        """
        index = value % self.table_size
        if self.table[index] is None:
            return index
        else:
            while self.table[index] is not None:
                index = (index + 1) % self.table_size
            return index

    def insert_value(self, value):
        index = self.linear_hash_function(value)
        self.table[index] = value

    def search(self, value):
        index = value % self.table_size

        if self.table[index] != value:
            while self.table[index] is not None and self.table[index] != value:
                index = (index + 1) % self.table_size
        if self.table[index] == value:
            print("Key is found in the table")
        else:
            print("key is not found in the table")

    def delete(self, value):
        index = value % self.table_size

        if self.table[index] != value:
            while self.table[index] is not None and self.table[index] != value:
                index = (index + 1) % self.table_size
        if self.table[index] == value:
            print("key {} is found in the table and hence deletion tag is updated at that position".format(value))
            self.table[index] = "Deletion"
        else:
            print("key {} is not found in the table and hence no deletion".format(value))


linear_probe_object = open_addressing_lp(10)
linear_probe_object.insert_value(4)
linear_probe_object.insert_value(44)
linear_probe_object.insert_value(54)
linear_probe_object.insert_value(55)
print("table is created...", linear_probe_object.table)
linear_probe_object.search(55)
linear_probe_object.search(56)
print("Going for deletion..........")
linear_probe_object.delete(55)
linear_probe_object.delete(56)
print("Final table after insertion, search and deletion.......")
print(linear_probe_object.table)
print("Going for more insertion and search......")
linear_probe_object.insert_value(99)
linear_probe_object.insert_value(64)
linear_probe_object.search(64)



class custom_hash_function:

    def __init__(self, bucket_size):
        """
        :input: bucket size to be inserted by the user
        :return: list of list
        """
        self.bucket_length = bucket_size
        self.bucket_table = [[] for i  in range(self.bucket_length)]

    def insert_element(self, value_to_be_inserted):
        """
        :input: value to be inserted
        :return: value is inserted at that position
        """
        bucket_index = value_to_be_inserted % self.bucket_length
        self.bucket_table[bucket_index].append(value_to_be_inserted)

    def search_element(self, element_to_be_searched):
        bucket_index = element_to_be_searched % self.bucket_length
        if element_to_be_searched in self.bucket_table[bucket_index]:
            return True
        else:
            return False

    def remove_element(self, element_to_be_removed):
        bucket_index = element_to_be_removed % self.bucket_length
        inner_bucket_list = self.bucket_table[bucket_index]
        if element_to_be_removed in inner_bucket_list:
            inner_bucket_list.remove(element_to_be_removed)
            print("Number {} is removed..".format(element_to_be_removed))
        else:
            print("You choosed the element which is not there in this hash table")


custom_hash_object = custom_hash_function(bucket_size=7)
print("Empty list inside main list:", custom_hash_object.bucket_table)
custom_hash_object.insert_element(8)
print("Inserted value inside the main list:", custom_hash_object.bucket_table)
search_element = custom_hash_object.search_element(8)
print("Search results in {} operation".format(search_element))
custom_hash_object.remove_element(8)
print("Go for another insertion, search and removal........")
custom_hash_object.insert_element(16)
print("Inserted value inside the main list:", custom_hash_object.bucket_table)
search_element = custom_hash_object.search_element(17)
print("Search results in {} operation".format(search_element))
custom_hash_object.remove_element(17)

import unittest

"""
input = [1, 1, 2]
output: 2 has one occurence and hence is add one out

input = [10, 10,20, 20, 20]
output: 10 has three occurence and is odd one out
"""


def detect_odd_count_element_from_list(input_list):
    # since this is a loop and there is no inner loop involved
    # hence the time complexity is o(n)
    for each in input_list:
        count_of_each_unique_element = input_list.count(each)
        if count_of_each_unique_element % 2 != 0:
            return each


class test_cases(unittest.TestCase):

    def cases_implement(self):
        """
        input is the list and output is an boolean expression
        """
        # case 1:
        input_list = [1, 1, 1, 2, 2]
        desired_output = 1
        actual_output = detect_odd_count_element_from_list(
            input_list=input_list
        )
        message = "Case 1(detect_odd_count_element_from_list)"
        self.assertEqual(desired_output, actual_output, message)

        # case 2:
        input_list = [1, 1, 2, 2, 3, 3, 4]
        desired_output = 4
        actual_output = detect_odd_count_element_from_list(
            input_list=input_list
        )
        message = "Case 2 (detect_odd_count_element_from_list)"
        self.assertEqual(desired_output, actual_output, message)

        return "Success..."


check_case = test_cases()
print(check_case.cases_implement())

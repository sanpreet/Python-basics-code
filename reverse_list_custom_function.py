import unittest

"""
reverse the list using the custom function
Idea is to keep on swapping the corner elements of the list
Condition to stop
Condition 1: if the list is odd then where the starting index and ending index meet stop
Condition 2: if the list is even then when the ending index passes the staring index stops
"""


def custom_function_for_reverse(input_list):
    n = len(input_list) - 1
    for i in range(n + 1):
        """
        condition for swapping the corner elements from both side
        """
        temp = input_list[n]
        input_list[n] = input_list[i]
        input_list[i] = temp
        """
        condition is applied for both even and odd list 
        """
        n = n- 1
        i = i + 1
        if i >= n:
            break
    return input_list


class test_cases(unittest.TestCase):

    def cases_implement(self):
        """
        input is the list and output is an reverse list
        """
        # case 1:
        input_list = [1, 1, 1, 2, 2]
        desired_output = [2, 2, 1, 1, 1]
        actual_output = custom_function_for_reverse(
            input_list=input_list
        )
        message = "Case 1(odd list)"
        self.assertListEqual(desired_output, actual_output, message)

        # case 2:
        input_list = [40, 50]
        desired_output = [50, 40]
        actual_output = custom_function_for_reverse(
            input_list=input_list
        )
        message = "Case 2 (even list)"
        self.assertListEqual(desired_output, actual_output, message)

        return "Success..."


check_case = test_cases()
print(check_case.cases_implement())
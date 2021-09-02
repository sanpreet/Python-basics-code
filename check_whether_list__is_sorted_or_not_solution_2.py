import unittest


def checking_list_is_sorted_or_not(checking_list):
    i = 1
    while(i < len(checking_list)):
        if checking_list[i] < checking_list[i - 1]:
            return False
        i += 1
    return True
                

class test_cases(unittest.TestCase):

     def cases_implement(self):   
        """
        input is the list and output is an boolean expression   
        """
        # case 1:
        input_list = [1, 2, 3, 4]
        desired_ouput = True
        actual_output = checking_list_is_sorted_or_not(
            checking_list=input_list
            )
        message="Case 1(list in sorted order) Fails"    
        self.assertEqual(desired_ouput, actual_output, message)

        # case 2:
        input_list = [1, 1, 2, 2]
        desired_ouput = True
        actual_output = checking_list_is_sorted_or_not(
            checking_list=input_list
            )
        message="Case 2 (same values) Fails:"    
        self.assertEqual(desired_ouput, actual_output, message)

        # case 3:
        input_list = [4, 1, 3, 2]
        desired_ouput = False
        actual_output = checking_list_is_sorted_or_not(
            checking_list=input_list
            )
        message="Case 3 (descending order) Fails:"    
        self.assertEqual(desired_ouput, actual_output, message)


        return "Success..."



check_case = test_cases()
print(check_case.cases_implement())
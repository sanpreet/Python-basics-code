"""
arr[] = {1, 5, 11, 5}
Output: true
The array can be partitioned as {1, 5, 5} and {11}
"""
import numpy as np
# import unittest


# arr = [1, 5, 11, 5]
def checks_equal_parition(arr):
    sum = 0
    for i in arr:
        sum += i

    if sum % 2 != 0:
        # print("this array does not contains two subarrays of equal size")
        return False
    else:
        target = sum // 2
        # knap sack algorithm
        # step 1: to create the matrix
        n = len(arr)
        np_matrix = np.zeros(
            [n + 1, target + 1],
            bool
        )
        # print(np_matrix.shape)
        # step 2: to make the first column of this matrix as True
        np_matrix[:, 0] = True
        # print(np_matrix)
        # step 3: To fill this matrix
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                # logic 1 if the array element is greater than target
                if j >= arr[i - 1]:
                    np_matrix[i][j] = (np_matrix[i - 1][j] +
                                    np_matrix[i - 1][j - arr[i - 1]])

                else:
                    np_matrix[i][j] = np_matrix[i - 1][j]

    boolean_output = np_matrix[n][target]
    if boolean_output:
        return True
    else:
        return False


array = [1, 5, 11, 5]
actual_output = True
desired_output = checks_equal_parition(arr=array)
# message = "Desired and actual values are not equal"
if desired_output == actual_output:
    print("Success...")
else:
    print("Failure")

array = [1, 5, 3]
actual_output = False
desired_output = checks_equal_parition(arr=array)
# message = "Desired and actual values are not equal"
if desired_output == actual_output:
    print("Success...")
else:
    print("Failure")

array = [1, 2, 3, 5]
actual_output = False
desired_output = checks_equal_parition(arr=array)
# a = ertyt
# message = "Desired and actual values are not equal"
if desired_output == actual_output:
    print("Success...")
else:
    print("Failure")

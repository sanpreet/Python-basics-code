"""
Bitwise solution to find the odd element from the list

Properties of bitwise
0 xor b = b
b xor b = 0
a xor b xor c =  b xor a xor c = c xor b xor a
for xor operation answer is one if both the bits are different
"""


def detect_odd_count_element_from_list(input_list):
    result_xor_operation = 0
    for each in input_list:
        result_xor_operation = result_xor_operation ^ each
    if result_xor_operation == 0:
        return None
    else:
        return result_xor_operation


user_list = [1, 1, 2, 2, 3]
odd_element = detect_odd_count_element_from_list(
    input_list=user_list
)
print("Show the odd element in the list i.e whose count is odd: {}".format(
    odd_element)
)

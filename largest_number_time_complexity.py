# program to find the largest of number in the iterable with time complexity theta(n**2)

list_of_numbers = [4, 3, 2, 1]


def function_to_find_largest_number_with_theta_n_square(iterable):
    """
    :param iterable:
    :return: largest number from the list
    since two loops are involved and one is inner loop \
    where n = length of list hence the time complexity is theta (n**2)
    """

    for x in iterable:
        for y in iterable:
            if y > x:
                break
        else:
            return x
    return None


largest_number_with_theta_n_square = function_to_find_largest_number_with_theta_n_square(list_of_numbers)
print("largest_number with theta nsquare:", largest_number_with_theta_n_square)


# program to find the largest number with the time complexity theta(n)
def function_to_find_largest_number_with_theta_n(iterable):
    """
    :param iterable:
    :return: largest number from the list
    since one loops are involved and one is inner loop \
    where n = length of list hence the time complexity is theta (n)
    """

    comparing_value = iterable[0]
    n = len(iterable)
    if not n:
        return None
    for i in range(1, n):
        if iterable[i] > comparing_value:
            comparing_value = iterable[i]
    return comparing_value


largest_number = function_to_find_largest_number_with_theta_n(list_of_numbers)
print(largest_number)
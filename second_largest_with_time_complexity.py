# program to find the largest of number in the iterable with time complexity theta(n)
# it will use two traversals
list_of_numbers = [4, 3, 2, 1]


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


# traversal 1
largest_number = function_to_find_largest_number_with_theta_n(list_of_numbers)
second_largest = None
for i in list_of_numbers:
    if i != largest_number:
        if second_largest is None:
            second_largest = i
        else:
            second_largest = max(second_largest, i)  # traversal 2

print("Second_largest number is: {}".format(second_largest))

# efficient solution to handle the above case with one traversal
# case 1:
# suppose we get the largest and second largest from the list from l0 to ln-1 \
# comparsion is made between ln-1 and ln. if ln is > ln-1 then largest becomes ln
# case 2:
# suppose we get the largest and second largest from the list from l0 to ln-1 \
# comparsion is made between ln-1 and ln. if ln is < ln-1
# case 2.1
# if ln > second_largest
# second_largest = ln
# case 2.2
# if ln < second_largest or second largest is none \
# ignore in this case
# case 3
# if ln == ln-1 then also ignore this case


def second_largest_with_one_traversal(iterable):
    if len(iterable) <= 1:
        return None
    lar = iterable[0]
    slar = None
    for x in iterable[1:]:
        if x > lar:
            slar = iterable[0]
            lar = x
        elif x != lar:
            if slar is None or slar < x:
                slar = x
    return slar


second_largest = second_largest_with_one_traversal(iterable=list_of_numbers)
print("Second_largest number is: {}".format(second_largest))


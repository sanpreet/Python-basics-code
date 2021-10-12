# solve this challenge: Rotate list to the left by n places
from collections import deque

list1 = [
    12, 34, 55, 66, 77
]
list1_copy = list1[:]
rotate_places_left = 3

# direct method 1
for i in range(rotate_places_left):
    removed_element = list1.pop(0)
    list1.append(removed_element)
#  direct method 2 slicing
new_list = list1_copy[rotate_places_left:] + list1_copy[:rotate_places_left]

# checking whether the method 1 and method 2 are giving the same output
# print(list1)

# method 3
# using deque method
dq_object = deque(list1_copy)
dq_object.rotate(-rotate_places_left)
final_list = list(dq_object)


# method 4 with time complexity theta(n) and space complexity as theta(1)
# since reverse at the max takes theta(n)
# since we are using the same list no auxiliary space is used hence the space complexity is theta(1)
def reverse_function(user_list, start_index, end_index):
    # base condition
    while start_index < end_index:
        user_list[start_index], user_list[end_index] = user_list[end_index], \
                                                       user_list[start_index]
        start_index += 1
        end_index -= 1
    return user_list


# step 1: reverse till d
list1_copy = reverse_function(user_list=list1_copy, start_index=0, end_index=rotate_places_left - 1)
# step 2: reverse elements after d
list1_copy = reverse_function(user_list=list1_copy, start_index=rotate_places_left, end_index=len(list1_copy) - 1)
# step 3: reverse the whole list
list1_copy = reverse_function(user_list=list1_copy, start_index=0, end_index=len(list1_copy) - 1)

if list1 == new_list == final_list == list1_copy:
    print("lists are equal and method {}, method {}, method {} and method {} are validated".format(1, 2, 3, 4)
          )
# what is left
# fixme: if len of list is empty and if rotation places are more than length of list

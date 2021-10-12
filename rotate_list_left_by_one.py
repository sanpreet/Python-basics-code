def rotate_list_by_one_left(user_list):
    """
    input: user list 
    output: same list which is left rotated by one
    Only one loop is used to make this operation so time complexity is o(n)
    since no other list is used hence the spacy complexity is constant 
    """
    n = len(user_list)
    last_index = n - 1
    temp = user_list[0]
    for i in range(last_index):
        user_list[i] = user_list [i + 1]
    user_list[last_index] = temp

    return user_list 


input_list = [
    4, 5, 6, 7, 3, 4, 1
    ]
input_list_method_1  = input_list[:]    

rotated_left_user_list = rotate_list_by_one_left(
    user_list=input_list
    )
print("Rotated list by one left by method 1 is: {}".format(rotated_left_user_list))     

# method 2
rotate_left_list_numbers = input_list_method_1[1:] + input_list_method_1[0:1]
print("Rotated list by one left by method 2 is: {}".format(rotate_left_list_numbers))
# method 3

input_list_method_1.append(input_list_method_1.pop(0))
print("Rotated list by one left by method 3 is: {}".format(input_list_method_1))

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

rotated_left_user_list = rotate_list_by_one_left(
    user_list=input_list
    )
print("Rotated list by one left is: {}".format(rotated_left_user_list))     
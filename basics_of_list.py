# code to get the element using the index
def get_by_index(arr,n,idx):
    try:
        output = arr[idx]
    except Exception as e:
        output = -1    
    return output

n = 6
arr = [
    1, 2, 3, 4, 5 , 6
    ]
index = 6

print(get_by_index(arr=arr, n=n, idx=index))

# code to delete the element at an index and then after delete shift all the elements after that index to one position left
# and append zero at the end

def del_by_index(arr,n,idx):
    del arr[idx]
    arr.append(0)
    return arr

n = 6
arr = [
    1, 2, 3, 4, 5, 6
    ]
index = 3

print(del_by_index(arr=arr, n=n, idx=index))

# count elements smallert than given element from the list
def count_smaller_than_x(arr,x):
    
    count = 0
    for i in arr:
        if i < x:
            count += 1
    print(count)


arr = [
    1, 2, 3, 4, 5, 6
    ]
x = 5
count_smaller_than_x(arr=arr, x=x)

def count_greater_than_x(arr,x):
    
    count = 0
    for i in arr:
        if i > x:
            count += 1
    print(count)


arr = [
    1, 2, 3, 4, 5, 6
    ]
x = 5
count_greater_than_x(arr=arr, x=x)

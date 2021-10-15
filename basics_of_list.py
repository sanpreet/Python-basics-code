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


def min_function(arr, n):
    
    smallest = arr[0]
    for i in range(n):
        if arr[i] < smallest:
            smallest = arr[i]
    
    return smallest


arr = [23, 1, 4, 0]
n = 4
print(min_function(arr=arr, n=n))


def max_function(arr, n):
    
    largest = arr[0]
    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]
    
    return largest


arr = [23, 1, 4, 0]
n = 4
print(max_function(arr=arr, n=n))


# Function to find median of the array
def median(A,N):
        
        A.sort()
        
        if len(A) % 2 != 0:
            # this says that number is odd
            # floor operation is used
            median = A[len(A) // 2]
            
        if len(A) % 2 == 0:
            index = int(len(A) / 2)
            number2 = A[index]
            number1 = A[index - 1]
            median = (number1 + number2) // 2
        return median

    
# Function to find mean of the array elements.   
def mean(A,N):
    sum_ = 0
    
    for i in A:
        sum_ += i
    mean = sum_ / N

    return mean 

N = 4
A = [2, 8, 3, 4]
median = median(A=A, N=N)
mean = mean(A=A, N=N)
print("Median of the array {} is {}".format(A, median))
print("Mean of the array {} is {}".format(A, mean))


# function to check whether the array is sorted in ascending or descending order
def is_sorted(array, size):
    # code here
    count = 0
    for i in range(size - 1):
        # condition to check the array sorting
        if array[i] <= array[i + 1]:
            count += 1
    # two conditions are applied one to check in ascending order and other in descending order
    if count == size - 1 or count == 0:
        return 1
    else:
        return 0


# conditions applied
n = 2
arr = [4, 2]
binary_result = is_sorted(array=arr, size=n)
print("Result of the array is::: {}".format(binary_result))

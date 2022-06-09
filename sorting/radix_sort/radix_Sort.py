def counting_sort(arr, exp):
    n = len(arr)
    radix_output = [0] * n
    # initialize count array as zero
    count_array = [0] * 10
    for i in range(n):
        index = arr[i] / exp
        count_array[int(index)%10] += 1
    for i in range(1, 10):
        count_array[i] += count_array[i - 1]
    # count_array
    # create the output array
    i = n - 1
    while i >= 0:
        index = arr[i] / exp
        radix_output[count_array[int((index)%10)] - 1] = arr[i]
        count_array[int((index)%10)] -= 1
        i -= 1

    for i in range(0, len(arr)):
        arr[i] = radix_output[i]


def radix_sort(arr):
    # find the max of the array
    max_element = max(arr)
    exp = 1
    while max_element / exp > 0:
        counting_sort(arr, exp)
        exp = exp * 10


arr = [319, 45, 19]
radix_sort(arr=arr)
print(arr)
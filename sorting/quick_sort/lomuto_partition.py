from re import L


def lomuto_partition(arr, low, high):

    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        # we have left the last element as it is the pivot element
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1] 
    
    return i + 1


array = [5, 3, 2, 1, 4]
index_pivot = lomuto_partition(arr=array, low=0, high=4)
print(array)
print("Index of pivot element is...{}".format(index_pivot))    

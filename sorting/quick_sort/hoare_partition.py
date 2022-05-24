def hoare_parition(arr, low, high):

    pivot =  arr[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -=1
        while arr[j] > pivot:
            j -= 1
        
        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]    


array = [14, 2, 13, 1, 5, 7]
index_j = hoare_parition(arr=array, low=0, high=len(array) - 1)
print(index_j)
print(array)

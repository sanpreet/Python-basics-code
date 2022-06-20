def first_occurence_binary_search(arr, search_element):

    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:

        mid = (low + high) // 2
        if arr[mid] > search_element:
            high = mid - 1

        elif arr[mid] < search_element:
            low = mid + 1

        else:
            if mid == 0 or arr[mid - 1] != arr[mid]:
                return mid
            else:
                high = mid - 1

    return -1


array = [1, 3, 3, 3]
searching = 3
print(first_occurence_binary_search(arr=array,
                                    search_element=searching))

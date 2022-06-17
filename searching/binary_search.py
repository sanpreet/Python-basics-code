# iterative approach of binary search
def binary_search(array, element_to_search):
    n = len(array)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if element_to_search == array[mid]:
            return mid
        elif element_to_search < array[mid]:
            high = mid - 1
        elif element_to_search > array[mid]:
            low = mid + 1

    return -1


array = [1, 3, 5, 7]
element_to_search = 8
print(binary_search(array=array,
                    element_to_search=element_to_search))
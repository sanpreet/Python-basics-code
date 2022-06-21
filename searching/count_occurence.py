def first_occurence(arr, element_search):
    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if element_search > arr[mid]:
            low = mid + 1
        elif element_search < arr[mid]:
            high = mid - 1
        else:
            if mid == 0 or arr[mid - 1] != arr[mid]:
                return mid
            else:
                high = mid - 1


def last_occurence(arr, element_search):
    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if element_search > arr[mid]:
            low = mid + 1
        elif element_search < arr[mid]:
            high = mid - 1
        else:
            if mid == n - 1 or arr[mid] != arr[mid + 1]:
                return mid
            else:
                low = mid + 1


def count_occurence(arr, element):

    first_index = first_occurence(arr=arr, element_search=element)

    if first_index == -1:
        return 0

    else:
        return (last_occurence(arr=arr, element_search=element) - first_index + 1)


array = [1, 3, 3, 3, 3, 3, 3, 3]
searching_element = 3
print(count_occurence(
    arr=array,
    element=searching_element)
)

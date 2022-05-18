def merge_subarrays(arr, low, mid, high):
    # create the left array
    left_arr = arr[low:mid + 1]
    right_arr = arr[mid + 1: high + 1]
    i = j = 0
    k = low
    len_i = len(left_arr)
    len_j = len(right_arr)

    while i < len_i and j < len_j:
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
            k += 1
        else:
            arr[k] = right_arr[j]
            j += 1
            k += 1

    while i < len_i:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len_j:
        arr[k] = right_arr[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):

    if right > left:
        mid = (right + left) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge_subarrays(arr, left, mid, right)
        


array = [10, 5, 30, 15, 7]
merge_sort(arr=array, left=0, right=len(array) - 1)
print(array)


def lomuto_partition(arr, l, h):
    i = l - 1
    pivot = arr[h]
    for j in range(l, h):
        # this means that it will not put any equal element to pivot to the left of the array
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1


def quick_sort(arr, l, h):
    if l < h:
        partittion = lomuto_partition(arr, l, h)
        quick_sort(arr, l, partittion - 1)
        quick_sort(arr, partittion + 1, h)


arr = [8, 4, 7, 9, 3, 10, 5]
low = 0
high = len(arr) - 1
quick_sort(arr=arr, l=low, h=high)
print(arr)

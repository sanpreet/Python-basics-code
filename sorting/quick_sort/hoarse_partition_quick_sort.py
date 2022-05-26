def hoarse_parition_quick_sort(arr, l, h):

    pivot = arr[l]

    i = l - 1
    j = h + 1

    while True:

        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def quick_sort_hoarse_partition(arr, l, h):
     if l < h:
         p = hoarse_parition_quick_sort(arr, l, h)
         quick_sort_hoarse_partition(arr, l, p)
         quick_sort_hoarse_partition(arr, p + 1, h)


arr = [8, 4, 7, 9, 3, 10, 5]
quick_sort_hoarse_partition(arr, 0, 6)
print(arr)

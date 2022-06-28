"""
Aim is to be find subarray from an array with sum = 0
Solution 1 : With time complexity O(n**2)
"""


def zero_sum_array(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n + 1):
            if sum(arr[i:j]) == 0:
                return True
    return False


arr = [1, 2, -3]
print(zero_sum_array(arr=arr))

"""
Solution 2 with time complexity 0(n)
"""


def zero_sum_array_hash_table(arr):
    pre_sum = 0
    comparison = set()  # set uses hash table at the backend
    for i in range(len(arr)):
        pre_sum += arr[i]
        if pre_sum == 0 or pre_sum in comparison:
            return True
        comparison.add(pre_sum)


arr = [1, 2, -3]
x = sum(arr)
print(zero_sum_array(arr=arr))

# using hashing
# using same array and length
arr = [2, 3, 4, 5, 11, 6]
n = len(arr)
sum_given = 10
hashmap = dict()
for i in range(n):
    temp = sum_given - arr[i]
    if temp in hashmap:
        print("pair is found which is ({}, {})".format(arr[i], temp))

    hashmap[arr[i]] = i


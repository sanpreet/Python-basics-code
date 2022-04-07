import numpy as np

arr = [2, 3, 4, 5, 11, 6]
sum_given = 13

n = len(arr)

# step 1 for knapsack is to initialize matrix of size (length of array + 1, sum_given + 1)
mat_np = np.zeros((n + 1, sum_given + 1))
# step 2: Fill the first column with true because there will be always a subset\
# which covers the condition that zero element and zero sum. Such subset is an empty subset
# base condition for recursive function becomes the initialization condition for top down approach
mat_np[:, 0] = 1
# print(mat_np)
# exit()
# step 3
# if the element taken from the array is > than sum given then that element is not
# included and if the element < sum given then there are two option either to include or
# not to include
# the purpose of this code is to cover the empty string in the array with true or false
for i in range(1, n + 1):
    for j in range(1, sum_given + 1):
        if j >= arr[i - 1]:
            mat_np[i][j] = (mat_np[i - 1][j] +
                            mat_np[i - 1][j - arr[i - 1]])

        else:
            mat_np[i][j] = mat_np[i - 1][j]
            # during exclude one needs to see that whether the sum can be achieved by the previous element of the array or not

total_subsets = 2 ** n
subsets_using_sum_given = int(mat_np[n][sum_given])
print(mat_np)
print("Total subsets which can are possible using given array are::: {}".format(total_subsets))
print("Total subsets which can be formed using given sum --{} are::: {}".format(sum_given, subsets_using_sum_given))
queue = list()
if mat_np[n][sum_given] > 0.0:
    queue.append(mat_np[n][sum_given])

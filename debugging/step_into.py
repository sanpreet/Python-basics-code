import numpy as np


def step_into(obj):

    result = np.sum(obj)

    return result


arr = [1, 3, 4]
sum_of_iterable = step_into(obj=arr)
print(sum_of_iterable)

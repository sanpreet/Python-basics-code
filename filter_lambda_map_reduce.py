# use case of apply and lambda
import pandas as pd
import functools

dictionary = {
    'Value 1': [12, 45, 77],
    'Value 2': [21, 54, 87]
}

df_frame = pd.DataFrame(
    dictionary
    )

df_squared = df_frame.apply(lambda x: x**2)
print("Use case of Lambda Function........")
print(df_squared)


# use case of the filter function python
# filter(function, sequence)
# filter function will those numbers from the sequence where the condition is true
def gett_square_of_even_number(number):
    if number % 2 == 0:
        return True
    return False


numbers = [1, 2, 3, 4]
even_number = filter(gett_square_of_even_number, numbers)
print()
print("Use case of Filter Function")
print(list(even_number))

# reduce function takes the function and iterable as arguments
# initializing list
lis = [1, 3, 5, 6, 2,]
# using reduce to compute sum of list
print()
print("Use case of Reduce function")
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, lis))


# map function takes function and iterable
def addition(n):
    return n + n


numbers = (1, 2, 3, 4)
print()
print("Use case of map function")
result = map(addition, numbers)
print(list(result))

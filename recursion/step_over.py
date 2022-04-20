def recursion_practice(n):
    # base condition
    if n == 0:
        return 0
    else:
        return recursion_practice(n - 1)


print(recursion_practice(3))

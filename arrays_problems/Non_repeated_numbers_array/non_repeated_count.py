def countNonRepeated(arr):

        dict_of_counts = {item:arr.count(item) for item in arr}
        count_non_repeated = 0
        for values in dict_of_counts.values(): 
            if values == 1:
                count_non_repeated += 1
        return count_non_repeated   


arr = [10, 20, 30, 40, 10]
print(countNonRepeated(arr=arr))

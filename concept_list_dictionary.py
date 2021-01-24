"""
You had bee provided cities and their temperature in the form of a list
You need to return the output in form of cities and mean of their temperature in
form of list.

See the below example for this

input = [['malout', 33.5], ['malout', 33.7], ['malout', 33.8], ['abohar', 48.2]]
output = [['malout', 33.66], ['abohar', 48.2]]
"""
import numpy as np

input_val = [
    ['malout', 33.5], ['malout', 33.7], ['malout', 33.8], ['abohar', 48.2]
]

# solution 1
empty_dict = dict()
for each_list in input_val:
    for each_element in each_list:
        if isinstance(each_element, str):
            if each_element in empty_dict:
                empty_dict[each_element] += 1
            else:
                empty_dict[each_element] = 1

temperature = list()
for each_list in input_val:
    if empty_dict[each_list[0]] > 1:
        temperature.append(each_list[1])
        mean_temperature = np.mean(temperature)
        mean_temperature = round(mean_temperature, 2)
        city = each_list[0]
        list1 = [city, mean_temperature]

    elif empty_dict[each_list[0]] == 1:
        mean_temperature = each_list[1]
        city = each_list[0]
        list2 = [city, mean_temperature]

final_list = [list1, list2]
print(final_list)

"""
Some discussions on the above code
Time complexity: Since outer and inner loops are involved to form a dictionary that \
counts number of appearance of each city hence time complexity is O(n**2)

Since empty dictionary and list takes extra space hence it will take spaces also

Also this code is not suitable for all test cases like what will happen if there are more number
of cities in the input but this is a fixed code where it will operate for only two cities

final_list = [list1, list2] is not optimized because what we will do if there are a lot of cities
we cannot manually add list there, It is a static solution. 
"""

# solution 2
cities = list()
for lists in input_val:
    for each_element in lists:
        if type(each_element) == str:
            if each_element not in cities:
                cities.append(each_element)

print("Number of cities present in the input are/is: {}".format(cities))

n = len(cities)
output_cities = [[]] * n
temp_list = list()
for i in range(n):
    for lists in input_val:
        if cities[i] in lists:
            city_name = lists[0]
            temp = lists[1]
            if len(temp_list) > 0:
                temp_list.append(temp)
            else:
                temp_list = [temp]
            mean_temp = np.mean(temp_list)
            mean_temp_round = round(mean_temp, 2)

    output_cities[i] = [city_name, mean_temp_round]
    temp_list = list()

print(
    "Result for Dynamic code for cities and their means is", output_cities
)

"""
Discussion of the above results
we are again using nested loop, hence time complexity is O(n**2)
I am also using list to append the output based on number of cities \
calculated and other list for appending all the temperatures of the \
same city. so space complexity is more than O(1) which i think is O(n)\

Let us talk about the problems being solved by this code
1.) You can add as many as cities and their temperatures 
 code will automatically calculate the results.
2.) Code is dynamic in nature

What to improve
===============

I am working on time and space complexity to reduced to O(n) 
"""


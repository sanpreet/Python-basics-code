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

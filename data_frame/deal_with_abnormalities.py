import pandas as pd

data_read = pd.read_csv('data.csv', encoding='utf-8')
# print(data_read)

# convert any string value to NaN Values 
data_read.column1 = data_read.column1.str.extract('(\d+)')
# convert the whole column to tge float type
data_read.column1 = data_read.column1.astype(float)
# check whether all the values are converted to float
for i in data_read.column1:
	print(type(i))

# mean value
mean_value = data_read.mean()
# fill the Nan Values with the mean
data_read = data_read.fillna(mean_value)
print(data_read)
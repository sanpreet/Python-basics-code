"""
Given dataframe with two columns date and values of different stocks

To make list equal to number of companies and each list will contain values
equal to length of all dates whereas dates where no result is there for any 
stocks such values are set to be empty

input
=====
toyota 2021-07-01    8.76
toyota 2021-07-02    8.86
toyota 2021-07-05    8.72
toyota 2021-07-06    8.75
microsoft  2021-08-01    271.6
microsoft  2021-08-02    267.29
microsoft  2021-08-05    271.49
microsoft  2021-08-06    271.58
apple  2021-09-01    137.27
apple  2021-09-02    133.75
apple  2021-09-05    137.13
apple  2021-09-06    137.13

output
======
dates = [2021-07-01 ,2021-07-02, 2021-07-05, 2021-07-06, 2021-08-01, 2021-08-02, 2021-08-05, 2021-08-06, 2021-09-01, 2021-09-02, 2021-09-05, 2021-09-06]
toyota_list = [8.76, 8.86, 8.72, 8.75, '', '', '', '', '', '', '', '']
microsoft_list = ['', '', '', '', 271.6, 267.29, 271.49, 271.58, '', '', '', '']
apple_list = ['', '', '', '', '', '', '', '', 137.27, 133.75, 137.13, 137.13]
"""
import pandas as pd

csv_file = 'data.csv'

data_frame_read = pd.read_csv(csv_file, header=None)
data_frame_read.columns = ['Company Name', 'Date', 'Prediction']
# print(data_frame_read)
# lets make a list of unique companies from the dataframe
unique_company_list = data_frame_read['Company Name'].unique().tolist()
# print("List of unique companies from the dataframe are: {}".format(unique_company_list))
unique_dates_list = data_frame_read['Date'].unique().tolist()
# print("List of unique dates from the dataframe are: {}".format(unique_dates_list))

sub_dict_store = dict()
for company in unique_company_list:
       sub_list = list()
       df_company = data_frame_read[data_frame_read['Company Name']==company]
       comp_pred_list = df_company['Prediction'].tolist()
       comp_date_list = df_company['Date'].tolist()       

       for index, date_value in enumerate(unique_dates_list):
              if date_value not in comp_date_list:
                     sub_list.append('')
              else:
                     sub_list.append(comp_pred_list[comp_date_list.index(date_value)])       
       sub_dict_store[company] = sub_list

for company, list_values in sub_dict_store.items():
    print(company,'=', list_values)   
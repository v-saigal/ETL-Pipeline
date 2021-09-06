import pandas as pd
from transform import clean_data 

#using one of the csv file as example
# df = pd.read_csv('././data/27/birmingham_27-08-2021_09-00-00.csv', header=None) 
data = clean_data('././data/27/birmingham_27-08-2021_09-00-00.csv')

# define column names
# df.rename(columns={0: "timestamp",
#                 1: "store_location",
#                 2: "customer_name",
#                 3: "basket",
#                 4:"payment_type",
#                 5:"total_price",
#                 6:"card_type"}, inplace=True)

# split the items example

def chunks(lst, n): #get the first order
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# item1 = df['basket'][0].split(',')[0] #get the first item of the first order
# print(item1)

# item2 = item1.split('-') #split by dash
# print(item2)

# print(item2[0].split(' ')[0]) #get size

#################################
# split out the elements in the items, extract the size of the whole basket column
#please copy this function into load_size form load.py

# def size():  

#     size_list = []

#     for x in df['basket']:  #split by comma and dash
#         item_list = x.split(',')
#         item2 = item1.split('-')

#         for n in item_list: #run through each item
#             each = n.split('-')
#             size_list.append(each[0].strip().split(' ')[0]) #first element in the item

#     unique_size = set(size_list) #makes unique size table
#     return unique_size

# # print(size())

#please copy this as an new function in transform.py
def get_unique_size(data):  #dictionary

    size_list = []

    for x in data:  #split by comma and dash
        item_list = x['basket'].split(',')

        for n in chunks(item_list,3): #run through each item
            # each = n.split('-')
            # size_list.append(each[0].strip().split(' ')[0]) #first element in the item
            size_list.append(n[0])
    unique_size = set(size_list) #makes unique size table
    return unique_size
    
print(size(data))
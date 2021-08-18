# # Fields include:
# # [Data&Time, Location, Full Name, Items & Price, payment type, total, card_type & card_number]

# fieldnames = ["timestamp","store_name","customer_name","basket", "payment_type", "total_price","card_number"]

# import pandas as pd 
# df = pd.read_csv('2021-02-23-isle-of-wight.csv')
# print(df.to_string()) # use pandas to print the data

from extract import extract, pathway
import csv, json

def extract_csv(): 
    with open('2021-02-23-isle-of-wight.csv', newline='') as csvfile:  
        reader = csv.DictReader(csvfile,fieldnames = ['Data', 'Time', 'Location', 'Full Name','Items', 'payment type', 'Price', 'card_type & card_number'])
        for row in reader:
            print(row['Data'], row['Time'], row['Location'], row['Full Name'], row['Items'], row['payment type'], row['Price'], row['card_type & card_number'])
# print(extract_csv())


def clean_basket(dict_list): # clean up basket
    
    for dict in dict_list: # print basket column
        # print(dict['basket'])
        basket_list = dict['basket'].split(',') # seperate items in basket
        # print(basket_list)
        
        store = []
        
        for item in basket_list:
            if len(item) == 0 :
                store.append('Regular') # replace size "space" into "regular"
            else:
                store.append(item)

        dict['basket'] = store
        print(dict['basket'])

        # print(store)
    return dict_list

print(clean_basket(extract(pathway)))













# from itertools import islice
# def seperate_basket_item(data, size):
#     it = iter(data)
#     for i in range(0, len(data), size):
#         yield {k:data[k] for k in islice(it, size)}

#     # for each_order in dict_list:
#     #     print(each_order, ':', basket_list[each_order])


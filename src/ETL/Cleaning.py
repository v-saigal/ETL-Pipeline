# # Fields include:
# # [Data&Time, Location, Full Name, Items & Price, payment type, total, card_type & card_number]

import csv

def extract_csv():  # Read file and give header
    with open('../../data/2021-02-23-isle-of-wight.csv', newline='') as csvfile:  
        reader = csv.DictReader(csvfile,fieldnames = ['Data', 'Time', 'Location', 'Full Name','Items', 'payment type', 'Price', 'card_type & card_number'])
        for row in reader:
            print(row['Data'], row['Time'], row['Location'], row['Full Name'], row['Items'], row['payment type'], row['Price'], row['card_type & card_number'])
# print(extract_csv())

def clean_basket(dict_list): # Clean up basket

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
# print(clean_basket(extract(pathway)))


# # Pandas
import csv
import pandas as pd 
# Make sure running this code in the correct directory (check terminal)

df = pd.read_csv('../../data/2021-02-23-isle-of-wight.csv', sep=',' , header=None)  # The first line would auto-assign as the header so we need to remove it
df.columns # The headers are now numbers we need to rename them.
df.rename(columns={0: 'date_time', 1: 'location', 2: 'full_name', 3: 'item_basket', 4: 'payment', 5: 'total_price', 6: 'card_type'}, inplace=True) 
df.dropna() # Delete NaN line
df.head() #showing first five lines
# df.shape # Check numbers of row and column
# df.dtypes # Check data type
print(df.to_string()) # Use pandas to print the data

# df.item_basket.fillna('Small') # Replace NaN into Small
split_basket_item = df['item_basket'].str.split(',',expand=True)  # Clean up basket. If expand is true pandas will make new columns for each value
split_basket_item.fillna('No specific size') # Replace NaN within the split basket 

split_basket_item.groupby('0')['1'].apply(list) # Grouping item column as order

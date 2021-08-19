from helper_modules.helper_funcs import pretty_print_dict
from cleaner import Cleaner
from extract import Extract

## Ignore this
# dummy_transaction = [
#     {'total': 22.0, 'item_basket': [
#         {'size':'large', 'product_name': 'tea', 'price': 2.20},
#         {'size': 'regular', 'product_name': 'coffee', 'price': 1.20}
#         ]},

#     {'total': 44.0, 'item_basket': [
#         {'size':'regular', 'product_name': 'chocolate tea', 'price': 2.3},
#         {'size': 'regular', 'product_name': 'lemon tea', 'price': 1.40}
#         ]},
# ]

# pretty_print_dict(dummy_transaction)
extract = Extract()

# This needs to run just once, need to update
def clean_data(extract):

    cleaner  = Cleaner()
    transaction_df = extract.extract_pandas()
    
    transaction_df.drop(columns="customer_name", inplace=True)
    
    # Remove card number, change case, replace blanks
    transaction_df["card_type"] = transaction_df["card_type"].apply(lambda x: cleaner.remove_card_number(x))
    transaction_df["basket"] = transaction_df["basket"].apply(lambda x: cleaner.replace_blanks(x))     
    transaction_df["basket"] = transaction_df["basket"].apply(lambda x: cleaner.change_case(x))   
    
    transaction_df.to_csv('../../data/cleaned_data.csv', sep=',', index=False)

clean_data(extract)

def transform_transaction_format(extract):
    data = extract.extract_dict("../../data/cleaned_data.csv")
    pretty_print_dict(data)
    
    store = []
    
    # This is used to make the basket table, each list contains each transaction,
    # which then has the specific quanity for that particular item

    for each_transaction in data:
        for keys in each_transaction:
            if keys == "basket":
                item_name = []
                store_unique_item_quanity = {}
                item_list = each_transaction[keys].split(',')
                for i in list(range(0, len(item_list), 3)):
                    item_name.append(item_list[i] + ' ' + item_list[i+1])
                unique_item = set(item_name)
                
                for item in unique_item:
                    store_unique_item_quanity[item] = item_name.count(item)
                
                store.append([store_unique_item_quanity])
                pretty_print_dict(store)
                
                
transform_transaction_format(extract)
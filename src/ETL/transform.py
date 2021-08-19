from extract import extract, pathway


def remove_card_number(df_value):
  
        if df_value == None:
            return df_value
    
        else:
            split = df_value.split(",")
    
            return split[0]
        

def remove_sensitive_data(transaction_df):
    
    transaction_df.drop(columns="customer_name", inplace=True)
        
    transaction_df["card_type"] = transaction_df["card_type"].apply(lambda x: remove_card_number(x))       
    
    print(transaction_df.head())
    
    return transaction_df    


def change_case(item_value):
    
    new_value = item_value.split(',')

    store = []
    
    for item in new_value:
        store.append(item.lower())
    
    return ','.join(store)


def apply_change_case(transaction_df):
    
    transaction_df["basket"] = transaction_df["basket"].apply(lambda x: change_case(x))       
    
    print(transaction_df.head())
    
    return transaction_df  



data = remove_sensitive_data(extract(pathway))
data = apply_change_case(data)

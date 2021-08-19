from extract import extract, pathway





def remove_sensitive_data(transaction_df):
    
    transaction_df.drop(columns="customer_name", inplace=True)
    print(transaction_df.head())
    
    col = 'card_type'
    for i in range(len(transaction_df[col])):
        
        current = transaction_df[col].iloc[i]
        
        if current == None:
            continue
       
        else:
            split = current.split(',')
            transaction_df[col].iloc[i] = split[0]
            
    print(transaction_df.head())
    return transaction_df    



data = remove_sensitive_data(extract(pathway))


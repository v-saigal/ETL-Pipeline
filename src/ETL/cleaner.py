class Cleaner:
    def __init__(self):
        print('starting to clean')

    def replace_blanks(self, item_value):
        new_value = item_value.split(',')
        store = []

        for item in new_value:
            if len(item) == 0:
                store.append('regular')
            else:
                store.append(item)
        
        return ','.join(store)

    def change_case(self, item_value):
        new_value = item_value.split(',')
        store = []

        for item in new_value:
            store.append(item.lower())

        return ','.join(store)
    
    def remove_card_number(self, df_value):
        if df_value == None:
            return df_value
        else:
            split = df_value.split(",")
            return split[0]
    def remove_numbers_card_type(self, df_value):
        if 'visa' in df_value:
            return df_value[:4]
        else:
            return df_value
    
    def comma_sep_splits(self, df_value):
        store = []
        split_each_item = df_value.split(',')
        
        for item in split_each_item:
            split_item_price = item.rsplit('-', 1)
            joined_clean_split_item_price = ','.join([x.strip() for x in split_item_price])
            
            split_each_category = joined_clean_split_item_price.split(" ", 1)
            store.append(','.join(split_each_category))
        
        return ','.join(store)
from extract import extract, pathway

keys_to_remove = ["customer_name", "card_number"]

def remove_keys(dict_list, keys_to_remove):
    for dict in dict_list:
        for key in keys_to_remove:
            del dict[key]
    return dict_list

data = remove_keys(extract(pathway), keys_to_remove)

print(data)
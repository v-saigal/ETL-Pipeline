def remove_keys(dict_list, keys_to_remove):
    for dict in dict_list:
        for key in keys_to_remove:
            del dict[key]
    return dict_list
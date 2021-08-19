import json
import pandas as pd

# Prints the json data in a pretty format
def pretty_print_dict(dict_file):
    print(json.dumps(dict_file, indent=2, sort_keys=True))

def save_df(df):
    df.to_csv('cleaned_data', sep=',', index=False)
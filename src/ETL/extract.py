import csv

import pandas as pd

pathway = "../../data/2021-02-23-isle-of-wight.csv"
fieldnames = ["timestamp","store_name","customer_name","basket", "payment_type", "total_price","card_type"]

class Extract:
    def __init__(self):
        print('Starting to extract')

    def extract_dict(self, pathway):
        with open(pathway, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            
            return list(reader)
    
    def extract_pandas(self):
        df = pd.read_csv(pathway, header=None)
        df.rename(columns={0: "timestamp",
                        1: "store_location",
                        2: "customer_name",
                        3: "basket",
                        4:"payment_type",
                        5:"total_price",
                        6:"card_type"}, inplace=True)
        return df
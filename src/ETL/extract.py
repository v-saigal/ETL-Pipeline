import csv
import json
from os import remove
import pandas as pd

pathway = "../../data/2021-02-23-isle-of-wight.csv"
fieldnames = ["timestamp","store_name","customer_name","basket", "payment_type", "total_price","card_type"]


def extract(pathway):
    df = pd.read_csv(pathway, header=None)
    df.rename(columns={0: "timestamp",
                       1: "store_location",
                       2: "customer_name",
                       3: "basket",
                       4:"payment_type",
                       5:"total_price",
                       6:"card_type"}, inplace=True)    
    print(df.head())    
    return df


extract(pathway)



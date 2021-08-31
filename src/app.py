from pandas.core.base import DataError
from ETL.load import load_transaction_side, load_size, load_product_side
from ETL.transform import clean_data     
import csv

def etl(data):
    data = clean_data(data)
    load_size(data)
    load_product_side(data)
    load_transaction_side(data)

with open("data/2021-02-23-isle-of-wight.csv", mode="r") as file:
    transaction_data = csv.reader(file)
    etl(file)
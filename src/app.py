from src.ETL.postgres_table import create_tables
from src.ETL.load import load_data
from src.ETL.transform import clean_data

def etl(data):
    create_tables()
    data = clean_data(data)
    load_data(data)

# def main():
#     with open("../data/birmingham_25-08-2021_09-00-00.csv", mode="r") as file:
#         transaction_data = csv.reader(file)
#         etl(file)

# main()
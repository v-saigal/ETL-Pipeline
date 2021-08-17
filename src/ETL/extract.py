import csv
import json

pathway = "../../data/2021-02-23-isle-of-wight.csv"
fieldnames = ['']

def extract(pathway):
    with open(pathway, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        
        for row in reader:
            print(json.dumps(row, indent=4, sort_keys=True))


extract(pathway)
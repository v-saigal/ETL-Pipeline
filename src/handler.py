import json
import boto3
import csv
from src.app import etl

import sys
print(sys.path)

def get_data(event):
    key = event['Records'][0]['s3']['object']['key']
    bucket = event['Records'][0]['s3']['bucket']['name']
    
    s3 = boto3.client('s3')
    s3_object = s3.get_object(Bucket = bucket, Key = key)
    data = s3_object['Body'].read().decode('utf-8')
    
    csv_data = csv.DictReader(data.splitlines())
    print(csv_data)
    
    return csv_data

def lambda_handler(event, context):
    # Get the s3 bucket triggered data
    data = get_data(event)
    # Run ETL process
    etl(data)
    
    return {
        'statusCode': 200,
        'body': json.dumps(data['Body'].read().decode('utf-8'))
    }


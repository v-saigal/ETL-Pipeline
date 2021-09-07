import boto3
import time
from src.app import etl
from io import StringIO

def get_data(event):
    key = event['Records'][0]['s3']['object']['key']
    bucket = event['Records'][0]['s3']['bucket']['name']
    
    print(key)
    # time.sleep(10)
    s3 = boto3.client('s3')
    s3_object = s3.get_object(Bucket = bucket, Key = key)
    data = s3_object['Body'].read().decode('utf-8')
    
    # Returns it in a format for pandas to work
    return StringIO(data)

def lambda_handler(event, context):
    # Get the s3 bucket triggered data
    data = get_data(event)
    # Run ETL process
    etl(data)
    
    return {
        'statusCode': 200,
        'body': 'Data has been loaded!'
    }


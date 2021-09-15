import json
import boto3
from io import StringIO
import re
import os


from src.ETL.transform import clean_data
from src.ETL.extract import Extract
import pandas as pd

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

def write_data(data, event):
    # Write clean data
    BUCKET = "team3-queue-test-clean"
    key = event['Records'][0]['s3']['object']['key']
    print(key.split('_'))
    # Separate the format to the whole filename
    key_split = key.split('.')
    # Get the dates from the filename
    re_search = re.search(r"[0-9]+-[0-9]+[0-9]-[0-9]*", key)
    re_date = re_search.group()
    print('date:', re_date)
    date_small_split = re_date.split('-')
    print('date_small_split:', date_small_split)
    # Year, months, day format
    file_name = f'clean_data/{date_small_split[2]}/{date_small_split[1]}/{date_small_split[0]}/{key_split[0]}.json'
    print('file_name', file_name)
    
    s3 = boto3.resource('s3')
    s3object = s3.Object(BUCKET, file_name)
    s3object.put(
        Body=(bytes(json.dumps(data).encode('UTF-8')))
    )
    
    return file_name


def lambda_handler(event, context):
    # Get the triggered data and clean it
    print('Running Lambda Handler')
    data = clean_data(get_data(event))
    print('Data now cleaned')
    file_name = write_data(data, event)
    
    sqs = boto3.client('sqs')
    queue_url = os.environ.get("QUEUE_URL")
    
    response = sqs.send_message(
        QueueUrl = queue_url,
        MessageBody = file_name
    )
    
    print('running:', file_name)
        
    return {
        'statusCode': 200,
        'Body': file_name
    }

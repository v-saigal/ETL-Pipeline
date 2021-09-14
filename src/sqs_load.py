import json
import boto3
from src.ETL.load import load_data

def open_file(file_name, bucket):
    s3 = boto3.client('s3')
    
    s3_object = s3.get_object(Bucket=bucket, Key=file_name)
    print('data in open_file:', s3_object['Body'])
    data = s3_object['Body'].read().decode('utf-8')
    
    return data


def lambda_handler(event, context):
    print(event)
    # sqs send method
    bucket = 'team3-queue-test-clean'
    file_name = event['Records'][0]['body']
    data = json.loads(open_file(file_name, bucket))
    
    print(data)
    print('loading')
    load_data(data)
    print('finished loading')
    
    # Old method, linking through functions
    # print(event['Records'])
    # print(event['Records'][0]['body'])
    
    # event_clean = json.loads(event['Records'][0]['body'])
    # print('event_clean', event_clean)
    # file_name = event_clean['responsePayload']['Body']
    # print('file_name', file_name)
    
    
    # data = open_file(file_name, 'team3-queue-test-clean')
    # new_d = json.loads(data)
    
    
    # print('data in final:', new_d)
    # print('loading ')
    # load_data(new_d)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Is this working Ruby?')
    }


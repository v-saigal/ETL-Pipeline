import json
import boto3
import os
import csv

def lambda_handler(event, context):
    # TODO implement
    data = tt()
    return {
        'statusCode': 200,
        'body': json.dumps(data['Body'].read().decode('utf-8'))
    }

def tt():
    # year, month, day
    key = '2021/8/25/birmingham_25-08-2021_09-00-00.csv'
    client = boto3.client('s3')
    
    data = client.get_object(Bucket='delon3-team-3-bucket', Key=key)
    return data

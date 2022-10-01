import boto3
import os
import requests
import tqdm

dynamo_client = boto3.resource(service_name='dynamodb', region_name='ap-south-1',
                               aws_access_key_id='AKxxxxxxxxxxxxxxxxx6ITOJHN67Z',
                               aws_secret_access_key='G7UW3J1tCtftMxxxxxxxxxxxxxxxxxxxxxxxxxxN')

product_table = dynamo_client.Table('slot-booking-app')
print(product_table.table_status)

import boto3

s3_client = boto3.client('s3')


s3_client.upload_file(
    './sherlock.txt',
    'mindsetcloud',
    'datalake-dio/data/sherlock.txt')

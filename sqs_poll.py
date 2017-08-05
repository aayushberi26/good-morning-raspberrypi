import boto3

from request_modules import display_data
from environment import (
    aws_access_key_id,
    aws_secret_access_key,
    aws_queue_url,
    aws_region_name
)

sqs = boto3.client('sqs',aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region_name)

def poll_and_run_script():
    while True:
        data = sqs.receive_message(
                    QueueUrl=aws_queue_url,
                    MaxNumberOfMessages=10,
                    WaitTimeSeconds=20
                )
        if 'Messages' in data:
            display_data()
            sqs.purge_queue(QueueUrl=aws_queue_url)            

if __name__ == '__main__':
    poll_and_run_script()


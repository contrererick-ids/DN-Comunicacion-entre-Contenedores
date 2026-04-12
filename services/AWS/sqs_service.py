import boto3

sqs_client = boto3.client('sqs')
SQS_URL="https://sqs.us-east-1.amazonaws.com/568257730157/cola-boletines.fifo"

def send_message(message_body):
    response = sqs_client.send_message(
        QueueUrl=SQS_URL,
        MessageBody=message_body,
        MessageGroupId='boletines_group'
    )
    return response
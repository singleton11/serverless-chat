import json
import time

import boto3

client = boto3.client('dynamodb')


def post(event, context):
    """Send message to the chat"""

    body = json.loads(event['body'])
    client.put_item(TableName='messages',
                    Item={
                        'message': {'S': body['message']},
                        'nick': {'S': body['nick']},
                        'created': {'N': str(int(time.time()))}
                    })

    return {'statusCode': 201}


def get(event, context):
    """Get all messages of the chat"""

    data = client.scan(TableName='messages')

    return {'statusCode': 200, 'body': json.dumps(data)}

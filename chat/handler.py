import json
import time

import boto3


def post(event, context):
    """Get all messages of chat"""

    client = boto3.client('dynamodb')

    body = json.loads(event['body'])
    client.put_item(TableName='messages',
                    Item={
                        'message': {'S': body['message']},
                        'created': {'N': str(int(time.time()))}
                    })

    return {'statusCode': 201}

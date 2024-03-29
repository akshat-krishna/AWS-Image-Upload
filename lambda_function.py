import json
import urllib.parse
import boto3

print('Loading function')

s3 = boto3.client('s3')
db = boto3.client('dynamodb', region_name = 'us-east-1')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    
    response = s3.get_object(Bucket=bucket, Key=key)
    item = {
        'file-name': {'S': str(key)},
        'content-type': {'S': str(response['ContentType'])},
        'last-update-time':{'S': str(response['LastModified'])},
        'image-size':{'N': str(response['ContentLength']/1000)},
    }
    response2 = db.put_item(TableName='mid-term-image-table', Item=item)
    return response['ContentType']

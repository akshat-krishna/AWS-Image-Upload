import pytest
from flask_testing import TestCase
from connect import app  # replace with the actual name of your Flask app file
from moto import mock_s3, mock_dynamodb2
import boto3
import io

class MyTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    @mock_s3
    def test_upload(self):
        # Setup mock S3
        s3 = boto3.client('s3', region_name='us-east-1')
        s3.create_bucket(Bucket='mid-term-image-bucket')
        
        response = self.client.post('/upload', data={
            'file': (io.BytesIO(b"dummy image data"), 'test.jpg')
        })
        
        assert response.status_code == 302  # assuming redirect on successful upload

    @mock_dynamodb2
    def test_display_data(self):
        # Setup mock DynamoDB
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        table = dynamodb.create_table(
            TableName='mid-term-image-table',
            KeySchema=[{'AttributeName': 'file-name', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'file-name', 'AttributeType': 'S'}],
            ProvisionedThroughput={'ReadCapacityUnits': 1, 'WriteCapacityUnits': 1}
        )
        table.put_item(Item={'file-name': 'test.jpg', 'description': 'Test Image'})

        response = self.client.get('/display-data/test.jpg')
        assert 'Test Image' in response.data.decode()

# Additional tests can be added here

if __name__ == '__main__':
    pytest.main()

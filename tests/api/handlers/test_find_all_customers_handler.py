import json
import pytest
from src.api.handlers.find_all_customers.find_all_customers_handler import find_all_customers_handler
from moto import mock_dynamodb2
import boto3

@pytest.fixture
def dynamodb():
    with mock_dynamodb2():
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        table = dynamodb.create_table(
            TableName='Customers',
            KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
            BillingMode='PAY_PER_REQUEST'
        )
        yield table

def test_find_all_customers_handler(dynamodb):
    dynamodb.put_item(Item={
        'id': '123',
        'name': 'John Doe',
        'cpf': '12345678901',
        'email': 'john.doe@example.com',
        'phone_number': '+1234567890'
    })
    
    event = {}
    
    response = find_all_customers_handler(event, None)
    body = json.loads(response['body'])

    assert response['statusCode'] == 200
    assert len(body) == 1
    assert body[0]['id'] == '123'

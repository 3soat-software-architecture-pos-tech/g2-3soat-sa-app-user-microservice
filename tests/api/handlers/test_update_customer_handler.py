import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src')))

import json
import pytest
from src.api.handlers.update_customer.update_customer_handler import update_customer_handler
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

def test_update_customer_handler(dynamodb):
    dynamodb.put_item(Item={
        'id': '123',
        'name': 'John Doe',
        'cpf': '12345678901',
        'email': 'john.doe@example.com',
        'phone_number': '+1234567890'
    })
    
    event = {
        'pathParameters': {'id': '123'},
        'body': json.dumps({
            'name': 'John Updated',
            'cpf': '12345678901',
            'email': 'john.updated@example.com',
            'phone_number': '+0987654321'
        })
    }

    response = update_customer_handler(event, None)
    body = json.loads(response['body'])

    assert response['statusCode'] == 200
    assert body['name'] == 'John Updated'
    assert body['email'] == 'john.updated@example.com'

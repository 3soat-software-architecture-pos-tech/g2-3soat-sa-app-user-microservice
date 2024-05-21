import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src')))

import json
import pytest
from src.api.handlers.add_customer.add_customer_handler import add_customer_handler
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

def test_add_customer_handler(dynamodb):
    event = {
        'body': json.dumps({
            'id': '123',
            'name': 'John Doe',
            'cpf': '12345678901',
            'email': 'john.doe@example.com',
            'phone_number': '+1234567890'
        })
    }

    response = add_customer_handler(event, None)
    body = json.loads(response['body'])

    assert response['statusCode'] == 201
    assert body['id'] == '123'
    assert body['name'] == 'John Doe'

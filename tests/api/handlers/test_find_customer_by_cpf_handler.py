import json
import pytest
from src.api.handlers.find_customer_by_cpf.find_customer_by_cpf_handler import find_customer_by_cpf_handler
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

def test_find_customer_by_cpf_handler(dynamodb):
    dynamodb.put_item(Item={
        'id': '123',
        'name': 'John Doe',
        'cpf': '12345678901',
        'email': 'john.doe@example.com',
        'phone_number': '+1234567890'
    })
    
    event = {
        'pathParameters': {'cpf': '12345678901'}
    }
    
    response = find_customer_by_cpf_handler(event, None)
    body = json.loads(response['body'])

    assert response['statusCode'] == 200
    assert body['id'] == '123'

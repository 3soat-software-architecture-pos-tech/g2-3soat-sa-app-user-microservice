import pytest
from src.infrastructure.dynamodb.customer_repository import DynamoDBCustomerRepository
from src.core.entities.customer import Customer
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
        yield dynamodb

@pytest.fixture
def repo(dynamodb):
    return DynamoDBCustomerRepository(dynamodb.Table('Customers'))

def test_add_customer(repo):
    customer = Customer(
        id='123',
        name='John Doe',
        cpf='12345678901',
        email='john.doe@example.com',
        phone_number='+1234567890'
    )
    repo.add(customer)
    item = repo.table.get_item(Key={'id': '123'}).get('Item')
    assert item['name'] == 'John Doe'

def test_find_customer_by_id(repo):
    repo.table.put_item(Item={
        'id': '123',
        'name': 'John Doe',
        'cpf': '12345678901',
        'email': 'john.doe@example.com',
        'phone_number': '+1234567890'
    })
    customer = repo.find_by_id('123')
    assert customer.id == '123'
    assert customer.name == 'John Doe'

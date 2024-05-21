import pytest
from src.core.entities.customer import Customer

def test_customer_creation():
    customer = Customer(
        id='123',
        name='John Doe',
        cpf='12345678901',
        email='john.doe@example.com',
        phone_number='+1234567890'
    )
    assert customer.id == '123'
    assert customer.name == 'John Doe'
    assert customer.cpf == '12345678901'
    assert customer.email == 'john.doe@example.com'
    assert customer.phone_number == '+1234567890'

import pytest
from src.core.use_cases.find_customer_by_id import FindCustomerByID
from src.core.entities.customer import Customer
from unittest.mock import Mock

def test_find_customer_by_id():
    repo = Mock()
    use_case = FindCustomerByID(repo)
    
    repo.find_by_id.return_value = Customer(
        id='123',
        name='John Doe',
        cpf='12345678901',
        email='john.doe@example.com',
        phone_number='+1234567890'
    )
    customer = use_case.execute('123')
    
    assert customer.id == '123'

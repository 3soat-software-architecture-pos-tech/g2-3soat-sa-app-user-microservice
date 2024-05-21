import pytest
from src.core.use_cases.add_customer import AddCustomer
from src.core.entities.customer import Customer
from unittest.mock import Mock

def test_add_customer():
    repo = Mock()
    use_case = AddCustomer(repo)
    
    customer = Customer(
        id='123',
        name='John Doe',
        cpf='12345678901',
        email='john.doe@example.com',
        phone_number='+1234567890'
    )
    use_case.execute(customer)
    
    repo.add.assert_called_with(customer)

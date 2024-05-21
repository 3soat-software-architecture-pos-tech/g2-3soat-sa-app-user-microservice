import pytest
from src.core.use_cases.update_customer import UpdateCustomer
from src.core.entities.customer import Customer
from unittest.mock import Mock

def test_update_customer():
    repo = Mock()
    use_case = UpdateCustomer(repo)
    
    customer = Customer(
        id='123',
        name='John Updated',
        cpf='12345678901',
        email='john.updated@example.com',
        phone_number='+0987654321'
    )
    use_case.execute(customer)
    
    repo.update.assert_called_with(customer)

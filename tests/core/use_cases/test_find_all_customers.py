import pytest
from src.core.use_cases.find_all_customers import FindAllCustomers
from src.core.entities.customer import Customer
from unittest.mock import Mock

def test_find_all_customers():
    repo = Mock()
    use_case = FindAllCustomers(repo)
    
    repo.find_all.return_value = [
        Customer(
            id='123',
            name='John Doe',
            cpf='12345678901',
            email='john.doe@example.com',
            phone_number='+1234567890'
        )
    ]
    customers = use_case.execute()
    
    assert len(customers) == 1
    assert customers[0].id == '123'

import pytest
from src.core.use_cases.find_customer_by_cpf import FindCustomerByCPF
from src.core.entities.customer import Customer
from unittest.mock import Mock

def test_find_customer_by_cpf():
    repo = Mock()
    use_case = FindCustomerByCPF(repo)
    
    repo.find_by_cpf.return_value = Customer(
        id='123',
        name='John Doe',
        cpf='12345678901',
        email='john.doe@example.com',
        phone_number='+1234567890'
    )
    customer = use_case.execute('12345678901')
    
    assert customer.id == '123'
    assert customer.cpf == '12345678901'

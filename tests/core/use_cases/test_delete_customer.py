import pytest
from src.core.use_cases.delete_customer import DeleteCustomer
from unittest.mock import Mock

def test_delete_customer():
    repo = Mock()
    use_case = DeleteCustomer(repo)
    
    use_case.execute('123')
    
    repo.delete.assert_called_with('123')

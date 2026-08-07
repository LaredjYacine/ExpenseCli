from CliExpenseTracker import Expense
import pytest
@pytest.fixture
def es():
    return Expense('text.txt')


def test_list(es):
    assert es.removeExpense(1) == True


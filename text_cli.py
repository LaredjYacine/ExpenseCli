from CliExpenseTracker import Expense
import pytest
@pytest.fixture
def es():
    return Expense('text.txt')


def test_list(es):

    assert es.addExpense('Food','33') == True


def test_list(es):
    es.save
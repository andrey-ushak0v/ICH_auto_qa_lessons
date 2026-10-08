import pytest
from calculator import Calculator


@pytest.fixture()
def create_calculator():
    return Calculator()
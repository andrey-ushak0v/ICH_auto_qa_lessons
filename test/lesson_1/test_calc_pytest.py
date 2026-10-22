import pytest

def test_sum_positive_numbers(create_calculator):
    assert create_calculator.sum(2,4) == 600
    assert create_calculator.sum(2, 5) == 7
    assert create_calculator.sum(1, 8) == 9


@pytest.mark.xfail(strict=True, reason="Метод в процессе разработки")
def test_sum_negative_numbers(create_calculator):
    assert create_calculator.sum(-2,-4) == -1000
    assert create_calculator.sum(-2, -5) == -7
    assert create_calculator.sum(-1, -8) == -9

@pytest.mark.skipif(condition="sys.version_info > (3, 8)", reason="Требуется Python 3.8 или выше")
def test_division(create_calculator):
    assert create_calculator.div(4, 2) == 2
    assert create_calculator.div(8, 2) == 4
    assert create_calculator.div(10, 5) == 2

def test_division_by_zero(create_calculator):
    with pytest.raises(ArithmeticError, match="Division by zero"):
        create_calculator.div(4, 0)
    print(11111)



@pytest.mark.skipif(condition="sys.version_info > (3, 8)", reason="pppppppp")
def test_division(create_calculator):
    assert create_calculator.div(4, 2) == 2
    assert create_calculator.div(8, 2) == 4
    assert create_calculator.div(10, 5) == 2

from part1 import *
import pytest

@pytest.mark.parametrize("input,expected",[("Hello",ValueError),(True,ValueError),(-1,ValueError),(None,ValueError),(100,'3.00'),(200.50,'6.01'),(1450,'45.75'),(5670.56,'193.47'),(12000,'420.00'),(30000.78,'1140.03'),(130000,'5290.00'),(450000.23,'19690.01')])
def test_calc_interest(input,expected):
    assert calculate_interest(input) == expected
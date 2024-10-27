import pytest
import os
import sys


sys.path.insert(0, r'C:\Users\Paulina\Desktop\test_actionsv2')
from src.libb import silnia_rekurencyjna


@pytest.mark.parametrize("n,expected_result", [(0, 1), (5, 120), (-1, 'Silnia jest zdefiniowana tylko dla liczb nieujemnych.')])
def test_silnia_args(n, expected_result):
    actual_result = silnia_rekurencyjna(n)
    assert expected_result == actual_result


def test_silnia_single():
    n = 5
    expected_result = 120
    actual_result = silnia_rekurencyjna(n)
    assert expected_result == actual_result

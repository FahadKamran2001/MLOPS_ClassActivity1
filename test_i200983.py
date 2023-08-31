"""
This module provides an implementation of the Fibonacci number calculation.
"""
from i200983 import fib_num
def test_fib_num():
    """
    Test function for the Fibonacci number calculation.

    This function asserts the expected values for various inputs of the 
    Fibonacci number calculation.
    """
    assert 0 == fib_num(1)
    assert 1 == fib_num(2)
    assert 1 == fib_num(3)
    assert 2 == fib_num(4)
    assert 3 == fib_num(5)
    assert 5 == fib_num(6)
    assert 8 == fib_num(7)
    assert 13 == fib_num(8)
    assert 21 == fib_num(9)
    assert 34 == fib_num(10)
    assert 55 == fib_num(11)
    assert 89 == fib_num(12)
    assert 144 == fib_num(13)
    
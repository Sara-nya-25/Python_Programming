"""
Comments have crept in instead of code in a few places. Finish writing the test cases test_empty_list and test_number_list.
# Returns the sum of all numbers in the list
def sum_list(list):
return None

def test_empty_list():
expected = # ???
actual = # ???
assert actual == expected

def test_number_list():
# TODO: test with lists that have one, two, and five elements, respectively.
assert sum_list([5]) == 5
assert # ???
assert # ???
"""
import pytest


# Returns the sum of all numbers in the list
def sum_list(num_list):
    return sum(num_list)


def test_empty_list():
    # The sum of an empty list is mathematically 0
    expected = 0
    actual = sum_list([])
    assert actual == expected


def test_number_list():
    # Test with one element
    assert sum_list([5]) == 5

    # Test with two elements (Equivalence Class: small list)
    assert sum_list([10, 20]) == 30

    # Test with five elements (Equivalence Class: larger list)
    assert sum_list([1, 2, 3, 4, 5]) == 15
"""
LAB_5/_2_assert.py::test_empty_list PASSED                                                                                                                                   [ 50%]
LAB_5/_2_assert.py::test_number_list PASSED                                                                                                                                  [100%]

"""
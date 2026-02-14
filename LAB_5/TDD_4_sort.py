"""
4 Consider the function is_sorted_ascending(numbers). It should return True if the list numbers is sorted in ascending order, False otherwise.
4a What equivalence classes does numbers have?
4b Formulate requirements and acceptance criteria for the function.
4c Write test cases for the function.
"""
import pytest

def is_sorted_ascending(numbers):
    if len(numbers) < 2:
        return True

    # Check if every element is <= the next element
    for i in range(len(numbers)-1):
        current_num = numbers[i]
        next_num = numbers[i+1]

        if current_num > next_num:
            return False

    return True

@pytest.mark.parametrize("input_list, expected", [
    ([], True),                 # Empty
    ([42], True),               # Single item
    ([1, 2, 3, 4, 5], True),    # Strictly ascending
    ([1, 2, 2, 3], True),       # Sorted with duplicates
    ([5, 4, 3, 2, 1], False),   # Strictly descending
    ([1, 3, 2], False),         # Out of order in middle
    ([1, 2, 3, 0], False),      # Out of order at end
    ([-10, -5, 0, 5], True),    # Negative numbers
    ([1,1,2], True)             # Ties, Duplicates
])

def test_is_sorted_ascending(input_list, expected):
    assert is_sorted_ascending(input_list) == expected

"""
Test results:
LAB_5/TDD_4_sort.py::test_is_sorted_ascending[input_list0-True] PASSED                                                                                                       [ 12%]
LAB_5/TDD_4_sort.py::test_is_sorted_ascending[input_list1-True] PASSED                                                                                                       [ 25%]
LAB_5/TDD_4_sort.py::test_is_sorted_ascending[input_list2-True] PASSED                                                                                                       [ 37%]
LAB_5/TDD_4_sort.py::test_is_sorted_ascending[input_list3-True] PASSED                                                                                                       [ 50%]
LAB_5/TDD_4_sort.py::test_is_sorted_ascending[input_list4-False] PASSED                                                                                                      [ 62%]
LAB_5/TDD_4_sort.py::test_is_sorted_ascending[input_list5-False] PASSED                                                                                                      [ 75%]
LAB_5/TDD_4_sort.py::test_is_sorted_ascending[input_list6-False] PASSED                                                                                                      [ 87%]
LAB_5/TDD_4_sort.py::test_is_sorted_ascending[input_list7-True] PASSED                                                                                                       [100%]
LAB_5/TDD_4_sort.py::test_is_sorted_ascending[input_list8-True] PASSED 
"""
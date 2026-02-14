"""
Balancing lists
As part of a larger program, we have a list that can contain multiple elements. But the elements can be moved between this and another list. We need a way to balance the lists, so that they have the same number of elements - at least as close as possible. The order of the elements is not important.

Formulate requirements and acceptance criteria.

Then run red-green-refactor for each acceptance criterion.
"""
def balance_lists(list_a, list_b):
    combined = list_a + list_b
    midpoint = len(combined) // 2
    return combined[:midpoint], combined[midpoint:]

# Test perfect and near balance
def test_balance_lengths():
    # Case 1: Even total (4 + 0) -> [2, 2]
    a, b = balance_lists([1, 2, 3, 4], [])
    assert len(a) == 2 and len(b) == 2

    # Case 2: Odd total (3 + 0) -> [1, 2] or [2, 1]
    c, d = balance_lists([1, 2, 3], [])
    assert abs(len(c) - len(d)) == 1


def test_data_integrity():
    list_a = ["apple", "banana"]
    list_b = ["cherry"]
    original_elements = sorted(list_a + list_b)

    new_a, new_b = balance_lists(list_a, list_b)
    assert sorted(new_a + new_b) == original_elements

"""
Test result
PASSED LAB_5/TDD_7_Balance_list.py::test_balance_lengths
PASSED LAB_5/TDD_7_Balance_list.py::test_data_integrity
"""
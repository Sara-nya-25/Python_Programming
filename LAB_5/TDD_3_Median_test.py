"""
3b Write test cases that test all ACs.

3c Implement the function so that all test cases are green.
"""
import pytest
from TDD_3_Median_num import find_median

@pytest.mark.parametrize("input_list, expected", [
    ([], None),                   # Empty list
    ([10], 10),                   # Single element
    ([1, 2, 1000], 2),            # Odd length
    ([1, 2, 3, 4], 2.5),          # Even length (avg of 2 and 3)
    ([-5, -1, -10], -5),          # Negative numbers
    ([1.5, 2.5, 5.0, 10.0], 3.75) # Floating point numbers
])

def test_find_median(input_list, expected):
    assert find_median(input_list) == pytest.approx(expected)

"""
Test results:
                                                                                                  

LAB_5/TDD_3_Median_test.py::test_find_median[input_list0-None] PASSED                                                                                                        [ 16%]
LAB_5/TDD_3_Median_test.py::test_find_median[input_list1-10] PASSED                                                                                                          [ 33%]
LAB_5/TDD_3_Median_test.py::test_find_median[input_list2-2] PASSED                                                                                                           [ 50%]
LAB_5/TDD_3_Median_test.py::test_find_median[input_list3-2.5] PASSED                                                                                                         [ 66%]
LAB_5/TDD_3_Median_test.py::test_find_median[input_list4--5] PASSED                                                                                                          [ 83%]
LAB_5/TDD_3_Median_test.py::test_find_median[input_list5-3.75] PASSED                                                                                                        [100%]

"""
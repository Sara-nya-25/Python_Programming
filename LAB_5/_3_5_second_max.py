"""
Winner takes it all is usually called, but now we will try to give some honor to all the second prize winners.
Formulate a test case for a function that finds the second largest number in a list!
# Returns the next largest number in the list
# Returns None if there is none
# If there is a tie for first place, that number is returned
def find_2nd_max(list):
"""
import pytest
# Function that finds the second max number in the list
def find_2nd_max(lst):
    if not lst:
        return None
    elif len(lst) == 1:
        return lst[0]
    else:
        lst.sort(reverse=True)
        return lst[1]

@pytest.mark.parametrize("input_list, expected", [
    ([], None),
    ([1], 1),
    ([2,4,6], 4),
    ([2,3,5,5,6,6], 6),
    ([-2,-3,-4,-6], -3)
    ])

def test_find_2nd_max(input_list, expected):
    assert find_2nd_max(input_list) == expected

"""
Test results:
LAB_5/_3_5_second_max.py::test_find_2nd_max[input_list0-None] PASSED                                                                                                         [ 20%]
LAB_5/_3_5_second_max.py::test_find_2nd_max[input_list1-1] PASSED                                                                                                            [ 40%]
LAB_5/_3_5_second_max.py::test_find_2nd_max[input_list2-4] PASSED                                                                                                            [ 60%]
LAB_5/_3_5_second_max.py::test_find_2nd_max[input_list3-6] PASSED                                                                                                            [ 80%]
LAB_5/_3_5_second_max.py::test_find_2nd_max[input_list4--3] PASSED 
"""

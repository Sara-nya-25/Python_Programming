"""
4 Formulate test cases for a function that finds the largest number in a list.
# Returns the largest number in the list
# Returns None if there is none
def find_max(list):
"""
import pytest
def find_max(numbers):
    if not numbers:
        return None

    current_max = numbers[0]
    for num in numbers:
        if num > current_max:
            current_max = num
    return current_max

@pytest.mark.parametrize("input_list, expected",[
    ([], None),
    ([42], 42),
    ([1,5,2],5),
    ([10,2,3],10),
    ([1,2,100],100),
    ([-5,-1,-10],-1),
    ([7,7,7],7)
])

def test_find_max(input_list, expected):
    assert find_max(input_list) == expected

"""
Test results:
LAB_5/_3_4_max_num.py::test_find_max[input_list0-None] PASSED                                                                                                                [ 14%]
LAB_5/_3_4_max_num.py::test_find_max[input_list1-42] PASSED                                                                                                                  [ 28%]
LAB_5/_3_4_max_num.py::test_find_max[input_list2-5] PASSED                                                                                                                   [ 42%]
LAB_5/_3_4_max_num.py::test_find_max[input_list3-10] PASSED                                                                                                                  [ 57%]
LAB_5/_3_4_max_num.py::test_find_max[input_list4-100] PASSED                                                                                                                 [ 71%]
LAB_5/_3_4_max_num.py::test_find_max[input_list5--1] PASSED                                                                                                                  [ 85%]
LAB_5/_3_4_max_num.py::test_find_max[input_list6-7] PASSED           
"""
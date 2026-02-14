"""
Complete the count_vowels function using the TDD method, red → green → refactor.
"""
def count_vowels_red(word):
    return None

def test_basic_vowel():
    assert count_vowels_red("apple") == 2

def count_vowels_green(word):
    # Minimal logic to pass the current test
    vowels = "aeiouyåäö"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

def test_uppercase_and_swedish():
    assert count_vowels_green("apple") == 2
    # Our current loop doesn't handle 'A' or 'Å' because it's case-sensitive
    assert count_vowels_green("Åse") == 2


def count_vowels_refactor(word):
    if not word:
        return 0

    target_vowels = "aeiouyåäö"
    # Refactored for readability and case-insensitivity
    return sum(1 for char in word.lower() if char in target_vowels)

import pytest

@pytest.mark.parametrize("input_str, expected", [
    ("qwrt", 0),          # No vowels
    ("apple", 2),         # Basic
    ("BANANA", 3),        # Uppercase
    ("Yxskaft", 2),       # Swedish 'y'
    ("åäö", 3),           # Swedish specific
    ("", 0),              # Empty string
    ("123!!", 0)          # Non-alphabetic
])
def test_count_vowels_comprehensive(input_str, expected):
    assert count_vowels_refactor(input_str) == expected

"""
Test results
collected 9 items                                                                                                                                                                 
LAB_5/_3_b_refactor.py::test_basic_vowel FAILED                                                                                                                              [ 11%]
LAB_5/_3_b_refactor.py::test_uppercase_and_swedish FAILED                                                                                                                    [ 22%]
LAB_5/_3_b_refactor.py::test_count_vowels_comprehensive[qwrt-0] PASSED                                                                                                       [ 33%]
LAB_5/_3_b_refactor.py::test_count_vowels_comprehensive[apple-2] PASSED                                                                                                      [ 44%]
LAB_5/_3_b_refactor.py::test_count_vowels_comprehensive[BANANA-3] PASSED                                                                                                     [ 55%]
LAB_5/_3_b_refactor.py::test_count_vowels_comprehensive[Yxskaft-2] PASSED                                                                                                    [ 66%]
LAB_5/_3_b_refactor.py::test_count_vowels_comprehensive[\xe5\xe4\xf6-3] PASSED                                                                                               [ 77%]
LAB_5/_3_b_refactor.py::test_count_vowels_comprehensive[-0] PASSED                                                                                                           [ 88%]
LAB_5/_3_b_refactor.py::test_count_vowels_comprehensive[123!!-0] PASSED   
"""
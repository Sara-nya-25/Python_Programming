"""
2a Consider the function count_words(sentence), which takes a string and returns the number of words. A word is a series of characters separated by spaces. Formulate the requirements and acceptance criteria (AC) that should apply to the function.

2b Write test cases that test all ACs.

2c Implement the function, so that all test cases turn green.
"""
import pytest
from TDD_count_words import count_words

@pytest.mark.parametrize("sentence, expected", [
    ("hello world", 2),          # Normal sentence
    ("", 0),                     # Empty string
    ("   ", 0),                  # Whitespace only
    ("hello    world", 2),       # More spaces in middle
    ("  hello world  ", 2),      # Leading or trailing spaces
    ("Python is fun!", 3),       # Extra Punctuation check
    ("P", 1)                     # Single letter
])

def test_count_words(sentence, expected):
    assert count_words(sentence) == expected

"""
Test results:
                                                                                                       [100%]
LAB_5/TDD_2_Count_words.py::test_count_words[hello world-2] PASSED                                                                                                           [ 16%]
LAB_5/TDD_2_Count_words.py::test_count_words[-0] PASSED                                                                                                                      [ 33%]
LAB_5/TDD_2_Count_words.py::test_count_words[   -0] PASSED                                                                                                                   [ 50%]
LAB_5/TDD_2_Count_words.py::test_count_words[hello    world-2] PASSED                                                                                                        [ 66%]
LAB_5/TDD_2_Count_words.py::test_count_words[  hello world  -2] PASSED                                                                                                       [ 83%]
LAB_5/TDD_2_Count_words.py::test_count_words[Python is fun!-3] PASSED
LAB_5/TDD_2_Count_words.py::test_count_words[P-1] PASSED                                                                                                                     [100%]
 
"""
"""
3a Discuss the following code. One test case is not enough to test the function - suggest more test cases, covering all the different possibilities for count_vowels.
# Returns an integer with the number of vowels in the word (aeiouyåäö)
def count_vowels(word):
return None

def test_no_vowels():
assert count_vowels("qwrt") == 0
assert count_vowels("Tt") == 0
assert count_vowels("123 123") == 0
assert count_vowels("") == 0

Tip 1: can the function find any vowels at all?
Tip 2: can it count all vowels?
Tip 3: can it count the same vowel if it occurs multiple times?
Tip 4: can it handle both uppercase and lowercase letters?
"""
def count_vowels(word):
    vowels = "aeiouyåäö"
    return sum(1 for char in word.lower() if char in vowels)

# Can the function find any vowels at all?
def test_single_vowels():
    assert count_vowels("a") == 1
    assert count_vowels("ö") == 1  # Testing Swedish specific vowels

# Can it count all vowels?
def test_all_vowels_set():
    # This ensures every character in your set is recognized
    assert count_vowels("aeiouyåäö") == 9

# test repeating vowels
def test_multiple_occurrences():
    assert count_vowels("banana") == 3
    assert count_vowels("Mississippi") == 4

# test both uppercase and lowercase
def test_case_insensitivity():
    assert count_vowels("Apple") == 2
    assert count_vowels("AÄÖ") == 3
    assert count_vowels("aäö") == 3

# test non-vowels and empty string
def test_no_vowels():
    assert count_vowels("qwrt") == 0
    assert count_vowels("123 123") == 0
    assert count_vowels("") == 0
"""
Test results
LAB_5/_3_a_vowel.py::test_single_vowels PASSED                                                                                                                               [ 20%]
LAB_5/_3_a_vowel.py::test_all_vowels_set PASSED                                                                                                                              [ 40%]
LAB_5/_3_a_vowel.py::test_multiple_occurrences PASSED                                                                                                                        [ 60%]
LAB_5/_3_a_vowel.py::test_case_insensitivity PASSED                                                                                                                          [ 80%]
LAB_5/_3_a_vowel.py::test_no_vowels PASSED 
"""
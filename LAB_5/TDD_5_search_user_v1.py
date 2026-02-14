"""
Searching for users
Imagine a function that can be used to display search results while the user types in a search field.
The function should take two parameters: input is what the user types, master_list is a list of options that can be found.
def autocomplete_list(input, master_list):

Start by formulating the requirements and acceptance criteria (AC) that should apply to the function.
Then choose an AC and write a test case. (red)
Then write code that satisfies the test case. (green)
Clean up the code, so you feel satisfied with your code so far. Then continue with the next AC.
"""

# Case insensivity handling
def autocomplete_list(input_str, master_list):
    results = []
    for item in master_list:
        if input_str.lower() in item.lower():   # handling case sensitive
            results.append(item)
    return results

def test_autocomplete_case_insensitivity():
    master = ["Apple", "Banana", "Apricot"]
    # Testing that 'ap' finds 'Apple' and 'Apricot' regardless of casing
    assert autocomplete_list("ap", master) == ["Apple", "Apricot"]

#PASSED LAB_5/TDD_5_search_user_v1.py::test_autocomplete_case_insensitivity

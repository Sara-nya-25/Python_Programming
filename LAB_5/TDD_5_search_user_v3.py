# The function should return items where the input string exists anywhere within the master_list item.

def autocomplete_list(input_str, master_list):
    if not input_str:
        return []

    normalized_input = input_str.lower()

    # Using 'in' allows the match to be anywhere in the string
    matches = [
        item for item in master_list
        if normalized_input in item.lower()
    ]

    return sorted(matches)

def test_autocomplete_fuzzy_match():
    master_list = ["Blueberry", "Strawberry", "Banana"]
    # Our previous code would return [] because neither starts with "berry"
    assert "Blueberry" in autocomplete_list("berry", master_list)
    assert "Strawberry" in autocomplete_list("berry", master_list)
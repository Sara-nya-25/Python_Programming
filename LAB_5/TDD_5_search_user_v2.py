# Empty Input handling
def autocomplete_list(input_str, master_list):
    results = []
    if not input_str:           # handling empty string
        return []
    for item in master_list:
        if input_str.lower() in item.lower():
            results.append(item)
    return results

def test_autocomplete_case_insensitivity():
    master = ["Apple", "Banana", "Apricot"]
    # Testing that 'ap' finds 'Apple' and 'Apricot' regardless of casing
    assert autocomplete_list("ap", master) == ["Apple", "Apricot"]
    assert autocomplete_list("", master) == []

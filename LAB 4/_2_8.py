"""
8 Make a function that can print the contents of a list a little more nicely.
First, the function should tell you if the list is empty, or how many elements it has.
Then the function should print the elements in a bulleted list. Example:
pretty_print(["a", "b", 3.14])
The list has 3 elements:
1. a
2. b
3. 3.14
"""
def pretty_print(lst):
    n = len(lst)
    index = 0
    if not n:
        print("Empty list")
    else:
        for i in range(n):
            index += 1
            print(f"{index}. {lst[i]}")

pretty_print(["a", "b", 3.14])

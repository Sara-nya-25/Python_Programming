"""
Write a function called last. It should take a list as a parameter and return the last element in the list.
last([1, 2, 3]) → 3
"""
def last_item(lst):
    if not lst:
        return "List is empty"
    return lst[-1]

print(last_item([1, 2, 3]))
print(last_item([10, 3, -4, -11]))
print(last_item([]))
print(last_item([100]))

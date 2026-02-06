"""
Write a function called cut_edges. It should take a list as a parameter. When called, it should return a new list, where it has removed the first and last elements.
cut_edges([1, 2, 3, 4]) → [2, 3]
"""
def cut_edges(lst):
    if len(lst) == 0:
        return "list is empty"
    elif len(lst) == 1:
        lst.pop(0)
        return lst
    lst.pop(0)
    lst.pop(-1)
    return lst

print(cut_edges([1, 2, 3, 4]))
print(cut_edges([]))
print(cut_edges([100]))
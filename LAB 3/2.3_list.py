# Manipulating List, List Functions

list_1 = [1,2,3,4,5,6,7,8,9,10, 'c','a','b','x','a','b','c']
list_2 = [1,5,6,55,6,8,9,22,12,8,9]

print("List 1: ",list_1)
print("Length of list_1= ", len(list_1))
print("Index of 5 in list_1 ",list_1.index(5))
print("count of 'a' in list_1 is ", list_1.count('a'))
print("Original List_2: ",list_2)
list_2.sort()
print("Sorted list_2", list_2)
list_2.reverse()
print("Reversed list_2: ",list_2)
list_2.append(4)
print("Append 4 to list_2:", list_2)
list_2.insert(5,66)
print("Insert 66 at index 5 to list_2:", list_2)
list_2.remove(6)
print("Remove 6 from list_2:", list_2)
popped = list_2.pop(0)
print("Remove number from index 0 :", list_2, "Popped number is ", popped)
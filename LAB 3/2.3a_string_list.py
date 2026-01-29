"""
3a Create a list with the names of four movies. The names should be strings. Print the entire list 2with the function print.
3b Add "Fellowship of the ring" to the last place in the list.
3c Add "The two towers" to the first place in the list. (index zero)
3d Find out what position (index) "Fellowship of the ring" now has.
3e Remove another of the movies. Has the Fellowship movie changed index?
3f Find out how long the list is. (len)
3g Reverse the list.
3h Sort the list in ascending alphabetical order.
"""
str_list = ['Star wars', 'Spider Man', 'The Lord of rings', 'Harry Potter']
print("Original list: ", str_list)
str_list.append("Fellowship of the ring")
print("\nAdding 'Fellowship of the ring' to list: ", str_list)
str_list.insert(0, "The two towers")
print("\nAdding 'The two towers' to list: ", str_list)
print("\nPosition of 'Fellowship of the ring' is ", str_list.index("Fellowship of the ring"))
print("\nLength of the string list : ", len(str_list))
str_list.reverse()
print("\nReversed list: ", str_list)
str_list.sort()
print("\nSorted list: ", str_list)


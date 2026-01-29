"""
Enter the following code and modify it so that it prints the figures a-j one at a time.
for y in range(1, 7):
s = ""
for x in range(1, 9):
if x == y:
s += "#"
else:
s += "."
print(s)
"""
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)
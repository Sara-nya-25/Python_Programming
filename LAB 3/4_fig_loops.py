print("Figure a")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 1:
            s += "#"
        else:
            s += "."
    print(s)

print("Figure b")


for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)

print("Figure c")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 3 or x == 4 or x == 5:
            s += "#"
        else:
            s += "."
    print(s)

print("Figure d")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 3 or y == 3:
            s += "#"
        else:
            s += "."
    print(s)

print("Figure e")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == (7-y) or x == 5:
            s += "#"
        else:
            s += "."
    print(s)

print("Figure f")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y or x == (7-y):
            s += "#"
        else:
            s += "."
    print(s)

print("Figure g")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x % 2 != 0:
            s += "#"
        else:
            s += "."
    print(s)
print()
print("Figure h")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        # Top and Bottom horizontal lines (Rows 2 and 5, between Columns 2-7)
        if (y == 2 or y == 5) and (2 <= x <= 7):
            s += "#"
        # Vertical sides (Columns 2 and 7, between Rows 2-5)
        elif (x == 2 or x == 7) and (2 <= y <= 5):
            s += "#"
        else:
            s += "."
    print(s)
print()
print("Figure i")
count = 0
a,b,c = 0,1,2
for y in range(0, 7):
    s = ""
    for x in range(0, 8):
        if count < 48:
            if count == a:
                a+=3
                s += "."
            elif count == b:
                b +=3
                s += "#"
            elif count == c:
                c +=3
                s += "O"
        count += 1
    print(s)

print("Figure j")

for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if y == 4:
            s += "."
        elif (y < 4 and x % 3 == 0) or (y == 5 and x % 2 == 0) or (y == 6 and x %2 != 0):
            s += "#"
        else:
            s += "."
    print(s)
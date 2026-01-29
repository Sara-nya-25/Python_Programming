for y in range(1,7):
    s = " "
    for x in range(1,9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)
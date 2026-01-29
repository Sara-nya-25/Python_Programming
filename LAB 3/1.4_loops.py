x = 0
y = 1
while y < 10:
    if y % 2 == 0:
        x-=y
    else:
        x += y * y

    y += 1
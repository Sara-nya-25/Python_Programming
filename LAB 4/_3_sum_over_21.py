"""
The 21 Game
If you add the numbers 1 + 2 + 3 + 4 + …, the sum of the numbers will get bigger and bigger.
Sooner or later you will get past 21. Write a function that prints the first number
in the number series that is bigger than 21.
"""
print("\n¤¤¤¤¤¤¤ 21 Game- In number series 1+2+3+4+..., print the first number in the number series that is bigger than 21.¤¤¤¤¤¤¤¤¤¤\n")
def first_over_21():
    total = 0
    number = 1
    while total <= 21:
        total += number
        if total > 21:
            print(f"The first number to push the sum over 21 is: {number}")
            print(f"The final sum was: {total}")
            break
        number += 1

first_over_21()

# Version 2: instead of using the number series, randomize numbers between 1 and 13. (the numbers in a regular deck of cards)
# Hint: import the random module and use the randint function to randomize numbers. Example: card = random.randint(1, 13)
import random
def random_first_over_21():
    total = 0
    lst = []
    print("\n***** First over 21 using Random number series *******\n")
    while total <= 21:
        number = random.randint(1, 13)
        total += number
        lst.append(number)
        if total > 21:
            print(f"The random number series generated: {lst}")
            print(f"The first number to push the sum over 21 is: {number}")
            print(f"The final sum was: {total}")
            break
        number += 1

random_first_over_21()
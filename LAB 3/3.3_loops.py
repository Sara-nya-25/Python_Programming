"""
Version 3: the program should ask how much percentage tip the user wants to add.
If the user doesn't type anything (empty string), the program should use 10% as the default.
Nice to have: try using try+except or isdigit to handle cases when the user types an incorrect value.
Python Try Except , isdigit | StackOverflow
"""
amount = 500
tips = input("How much percentage do you want to tip: ")
default_tip = 10
try:
    tips = int(tips)
    if tips:
        print(f"Tipped amount is {amount * tips/100}")
    else:
        print(f"Tipped amount is {amount * 10 / 100}")
except Exception as e:
    print("Enter a valid number")
    print(f"Default tip calculated:- Tipped amount is {amount * 10 / 100}")
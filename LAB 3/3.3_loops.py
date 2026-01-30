"""
Version 3: the program should ask how much percentage tip the user wants to add.
If the user doesn't type anything (empty string), the program should use 10% as the default.
Nice to have: try using try+except or isdigit to handle cases when the user types an incorrect value.
Python Try Except , isdigit | StackOverflow
"""
number_list = []
input_var = ''
total_amt = 0
print("***** Welcome to Receipt Buddy! Exit by typing:'q' quit ********")
try:
    while input_var != 'q':

        input_var = input("\nEnter an amount or press 'q' to quit: ")
        if input_var.lower() == 'q':
            break
        else:
            number_list.append(int(input_var))

    if len(number_list) > 0:
        print("Numbers Entered are: ", number_list)
        total_amt = sum(number_list)
        print("Total amount collected is ", total_amt,"kr")
    else:
        print("No numbers entered")

    default_tip = 10
    tips = input("How much percentage do you want to tip: ") or default_tip
    tips = int(tips)
    if tips != 10:
        tip_amt = total_amt * tips / 100
        print(f"Tipped amount is {tip_amt}")
    else:
        tip_amt = total_amt * 10 / 100
        print(f"Default tip calculated:- Tipped amount is {tip_amt} kr")

    total_amt = total_amt - tip_amt
    print(f"Total amount  {total_amt} kr")
    print("\n*** Party share calculator ****")
    num_of_person = int(input("Enter number of people: "))
    print(f"The amount {total_amt} kr is shared between {num_of_person} people.")
    print(f"The share is {total_amt / num_of_person:.2f} kr per person. Welcome back!")
except ValueError:
    print("Invalid input")



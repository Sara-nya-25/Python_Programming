"""
Write a program that repeatedly asks the user to enter a number. When the user enters the string "quit" or "quit", the program should calculate the sum of the numbers. Example:
Welcome to Receipt Buddy! Exit by typing: quit
Enter an amount: 25
Enter an amount: 50
Enter an amount: quit
That makes 75 SEK in total. Welcome back!
Tip! To solve the problem you need: several variables, input, while loop.
"""
number_list = []
input_var = ''
print("Welcome to Receipt Buddy! Exit by typing:'q' quit")
try:
    while input_var != 'q':

        input_var = input("\nEnter an amount or 'q' to quit: ")
        if input_var.lower() == 'q':
            break
        else:
            number_list.append(int(input_var))


    if len(number_list) > 0:
        print("Numbers Entered are: ", number_list)
        print(" Total amount: ", sum(number_list),'kr')
    else:
        print("No numbers entered")
except ValueError:
    print("Invalid input")

"""
Version 1:
100
10, 20, 15

"""
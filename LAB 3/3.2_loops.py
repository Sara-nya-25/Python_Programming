"""
Version 2: The program will ask how many people there are, and tell you how much each person in the party should pay.
How many of you are there? 3
That will be 75 SEK in total, or 25.0 SEK per person. Welcome back!
"""
number_list = []
input_var = ''
total_amt = 0
print("***** Welcome to Receipt Buddy! Exit by typing: 'q' quit ********")
try:
    while input_var != 'q':
        input_var = input("\nEnter an amount or 'q' to quit: ")
        if input_var.lower() == 'q':
            break
        else:
            number_list.append(int(input_var))

    if len(number_list) > 0:
        print("Numbers Entered are: ", number_list)
        total_amt = sum(number_list)
        print("Total amount collected", total_amt)
    else:
        print("No numbers entered")

    print("\n*** Party share calculator ****")
    num_of_person = int(input("Enter number of people: "))
    print(f"The amount {total_amt} is shared between {num_of_person} people.")
    print(f"The share is {total_amt / num_of_person:.2f} kr. Welcome back!")
except ValueError:
    print("Invalid input")

"""
Version 2:
100, 1 person
100, 2 personer
10, 10, 40 personer
30, 20, 30, 1 person
"""
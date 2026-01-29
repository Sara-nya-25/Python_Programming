"""
Todo list
Build a program that allows the user to add items to a todo list.
Hint: use a loop, input, and a variable for the list.
Example:

** Todo list extravaganza **
1. View the contents of your list
2. Add new items to your list
Choose an option: 1
Your list is empty
.
Choose an option: 2
Enter a new thing you need to remember to do: feed the goldfish
Ok, added "feed the goldfish" to the list.
.
Choose an option: 1
+ Feed the goldfish
"""
print("********************* Todo list extravaganza *************************")
print("Press 1: To view contents of your list ")
print("Press 2: Add new items to your list ")
print("Press 3: Exit")
option = 0
list_1 = []
while option != 3:
    try:
        option = int(input("\nEnter your choice: "))
        if option == 1:
            if len(list_1) == 0:
                print("No items added")
            else:
                print(f"List Contents: ")
                for i, item in enumerate(list_1):
                    print(f" Item {i+1}: {item}")
        elif option == 2:
            list_1.append(input("Enter your new item: "))
    except ValueError:
            print("Invalid option")

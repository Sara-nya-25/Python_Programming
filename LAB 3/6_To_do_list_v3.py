"""
Version 3: move completed items to a new list.
The user should be able to select what they have previously checked off,
or choose to put the item back on the todo list.
"""
print("********************* Todo list extravaganza *************************")
print("Press 1: To view contents of your list ")
print("Press 2: Add new items to your list ")
print("Press 3: To Mark an item as done")
print("Press 4: List History ")
print("Press 5: Exit")
option = 0
list_1 = []
history_list = []
while option != 5:
    try:
        option = int(input("\nEnter your choice(1.View list,2.Add new item,3.Mark as done,4.History, 5.Exit): "))
        if 0 < option < 6:
            if option == 1:
                if len(list_1) == 0:
                    print("No items added")
                else:
                    print(f"List Contents: ")
                    for i, item in enumerate(list_1):
                        print(f" Item {i+1}: {item}")
            elif option == 2:
                list_1.append(input("Enter your new item: "))
            elif option == 3:
                print(f"List Contents: ")
                for i, item in enumerate(list_1):
                    print(f" Item {i + 1}: {item}")
                remove_item = int(input("\nEnter the item you want to mark as done: "))
                popped_item = list_1.pop(remove_item-1)
                history_list.append(popped_item)
                print(f"'{popped_item}' Marked as done.")
            elif option == 4:
                if not history_list:
                    print("History list is empty")
                else:
                    for i, item in enumerate(history_list):
                        print(f" Item {i + 1}: {item}")
                    choice = input("Do you want to move an item from this list to to do list (Y/N)?")
                    if choice.lower() == 'y':
                        idx = int(input("\nEnter the new item number you want to add: "))
                        restored_item = history_list.pop(idx-1)
                        list_1.append(restored_item)
                        print(f"'{restored_item}' moved back to To-Do.")
        else:
            print("Invalid option!")
    except ValueError:
            print("Invalid input!")

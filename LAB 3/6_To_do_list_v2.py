"""
Version 2: add a menu item, "Mark as done". When the user selects it,
the program should ask which item is done. The completed item should be removed from the list.
"""
print("********************* Todo list extravaganza *************************")
print("Press 1: To view contents of your list ")
print("Press 2: Add new items to your list ")
print("Press 3: To Mark an item as done")
print("Press 4: Exit")
option = 0
list_1 = []
while option != 4:
    try:
        option = int(input("\nEnter your choice(1.View list, 2.Add new item, 3.Mark as done, 4.Exit): "))
        if 0 < option < 5:
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
                print(f" {remove_item} 'Marked as done' ")
                list_1.pop(remove_item-1)
        else:
            print("Invalid option")
    except Exception as e:
            print(f"Invalid input! Exception: {e}")

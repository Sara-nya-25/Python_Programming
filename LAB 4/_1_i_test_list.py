"""
A task in three parts:
List out what the function's purpose is, based on name and context.
List out what the expected result should be for the three test lists.
Fix the errors, so the function does what it's supposed to do.
"""
print("Function used to find the smallest number in a list ")
def find_min(numbers):
    counter = 0
    for item in numbers:
        if item < counter:
            counter = item
    print(f"The smallest item is: {counter}")
    return counter

find_min([10, 3, -4, -11])
find_min([])
find_min([100])
print("output is -11, 0, 0, in the third output should be 100, so slightly modify the function to get the desired result")

print("\n version 1: Including the condition to check the list with 1 element")
def find_min_v1(numbers):
    counter = 0
    for item in numbers:
        if len(numbers) == 1:
            counter = item
        elif item < counter:
            counter = item
    print(f"The smallest item is: {counter}")
    return counter

find_min_v1([10, 3, -4, -11]) # output -11
find_min_v1([]) # output 0
find_min_v1([100]) # output 100

print("\n Version 2: Pythonic way of doing it, handling empty list")
def find_min_v2(numbers):
    # Handle the empty list case
    if not numbers: # pythonic way
        print("The list is empty.")
        return None

    # Initialize with the first element of the list
    minimum = numbers[0]

    # Compare the rest of the items
    for item in numbers:
        if item < minimum:
            minimum = item

    print(f"The smallest item is: {minimum}")
    return minimum

find_min_v2([10, 3, -4, -11])  # Output: -11
find_min_v2([])
find_min_v2([100])  # Output: 100
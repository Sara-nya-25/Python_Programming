"""
The program should tell you if two of the numbers are equal, or all three are equal.
"""
print("Note: Numbers Entered should be integers.")
num_1 = int(input("Enter First number: "))
num_2 = int(input("Enter Second number: "))
num_3 = int(input("Enter Third number: "))
print("- "*35)
print(f"\nThe sum is {num_1 + num_2 + num_3}.")

if num_1 == num_2 == num_3:
    print("All three numbers are equal.")
elif num_1 == num_2 or num_2 == num_3 or num_3 == num_1:
    print("Two of the numbers are equal.")
else:
    print("All three are different.")

if num_1 >= num_2 and num_1 >= num_3:
    print(f"{num_1} is the largest number.")
elif num_2 >= num_1 and num_2 >= num_3:
    print(f"{num_2} is the largest number.")
else:
    print(f"{num_3} is the largest number.")

#Test data set: 1 2 3, 1 3 2, 3 2 1, -1 -3 -1, 9 9 9, 32 32 16
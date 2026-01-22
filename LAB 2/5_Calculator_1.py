"""
Make a program that asks the user for 3 numbers.
Then it should calculate the sum, and print it on the console.
(sum: number1 + number2 + number3)
"""
print("Note: Numbers Entered should be integers.")
num_1 = int(input("Enter First number: "))
num_2 = int(input("Enter Second number: "))
num_3 = int(input("Enter Third number: "))
print("- "*35)
print(f"\nThe sum is {num_1 + num_2 + num_3}.")

#Test data set: 1 2 3, 1 3 2, 3 2 1, -1 -3 -1, 9 9 9, 32 32 16
"""
A program to tell the user is eligible for a ride if user is 130cm tall or more
Test User Input: 121, 130, 155, 129
"""
print("Balder på Liseberg")
User_height = int(input("Enter Your Height: "))
if User_height >= 130:
     print("You can ride!!!")
else:
     print("You can't ride!!! Minimum Height 130 cm")

# As a tester it is always essential to test the boundary values and edge cases to find for errors



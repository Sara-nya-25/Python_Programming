"""
Program to apply discount to a product based on purchase value
Improving the code that has some errors
is_member = False
level1 = 100
level2 = 300
discount = 0
price = input("Köp något dyrt: ")
price = float(price)
if price > level1:
    print("Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
    discount = discount + 10
if price >= level2:
    print("Grattis! Du har avancerat till nivå 2 och får 25% rabatt.")
    discount = discount + 25

final_price = price * (100- discount)/100
print("Efter rabatter blir priset.... " + final_price)
"""
#is_member = False # This variable can be removed since, it's not used anywhere in the program
level1 = 100
level2 = 300
discount = 0
# Customer needs to be aware of the discount
# Display the discounts offered for the price to customer
print("Shop for minimum 100 Kr to get 10% discount and more than 300 kr to get 25% discount.")
price = input("Enter the purchase amount: ")
price = float(price)
# First we need to check the higher level(300) so that we dont apply the low and high discounts at the same time
# if we check for 100 & then 300 then both 10 & 25% will be applied
if price >= level2: # First we need to check discount is more than or equal to 300
    print("\nCongratulations! You got 25% discount....")
    discount = discount + 25
elif price >= level1: # If = not there then discount will not be applied if a person shops for 100
    print("\nCongratulations! You got 10% discount....")
    print(f"\nSuggestion: Shop some more for {level2- price} kr to get 25% discount.")
    discount = discount + 10
else:
    print("\nNo discounts applied. Shop for minimum 100 Kr to get 10% discount.")
    print(f"\nSuggestion: Shop some more for {level1- price} kr to get 10% discount or {level2- price} kr to get 25% discount.")

# in previous logic 100-discount is logic fail, it will reverse the 10 % discount to 90%
final_price = price * (100-discount)/100
# if we use + in print then the variable should be a string not a float
print("*"*100)
print("\nTotal Price after discount .... " + str(final_price) +' kr')

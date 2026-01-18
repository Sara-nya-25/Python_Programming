"""
Given Jacket Price = 2000
Get Discount Percent from user
Calculate the price of product after applying discount and print the same
"""
original_price = 2000

# Getting Discount percent as input
sale_percent = int(input("Enter the percentage of discount: "))

#Calculating the discounted amount
discount = original_price * sale_percent / 100

#Calculating the final price of the product after applying discount
final_price = original_price - discount

print("Original Price of jacket is ", original_price)
print("Discount percent = ", sale_percent, '%')
print("Your Savings = ", discount, 'kr')
print("The final price of the jacket is ", final_price,'kr')

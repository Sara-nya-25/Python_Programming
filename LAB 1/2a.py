"""
Given Jacket Price = 2000
Discount Percent = 75 %
Calculate the price of product after applying discount
"""
original_price = 2000
sale_percent = 75

# Calculating the discounted amount
discount = original_price * sale_percent / 100

# Calculating the Final price of product after applying discount
final_price = original_price - discount

print("Original Price of jacket is ", original_price, 'kr')
print("Discount percent = ", sale_percent, '%')
print("Final price of jacket is ", final_price, 'kr')
print("Your Savings = ", discount, 'kr')
print("The final price of the jacket is ", final_price, 'kr')

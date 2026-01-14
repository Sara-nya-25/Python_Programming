# calculate the price of product after applying discount

original_price = 2000
print("Original Price of jacket is ", original_price)
sale_percent = int(input("Enter the percentage of discount: "))
discount = original_price * sale_percent / 100
final_price = original_price - discount

print("Discount percent = ", sale_percent)
print("Discount = ", discount)
print("The final price of the jacket is ", final_price)

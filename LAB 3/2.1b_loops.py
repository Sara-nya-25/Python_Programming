"""
1b Calculate the sum of all numbers between 1 and 100. (including 1 and 100, the correct answer should be 5050)
"""
total_sum = 0
for i in range(1,101):
    total_sum += i

print("\nSum of numbers from 1 to 100 inclusive of 1 & 100 is ", total_sum)
"""
7 Build a function called average. It should take parameters: x and y.
Both should be numbers. The function should return the average.
For example, you calculate the average of 4 and 8 using the formula: (4 + 8) / 2, which is 6.
Tip: it can be easier to use more variables.
"""
def average(x,y):
    return (x + y)/2

print(f"Average of 2 numbers(4,8): {average(4,8)}")

print("\nImproving the function to calculate average of list of numbers")
def average_lst(lst):
    return sum(lst)/len(lst)

lst_1 = [1,5,8,9,10,25,18]
print(f"List: {lst_1}")
print(f"Average of list of numbers: {average_lst(lst_1):.2f}")
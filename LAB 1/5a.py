# Find length of the hypotenuse of a right-angled triangle.
# Given triangle with sides 3,4
import math

side_a = 3
side_b = 4

print('Given length of 2 sides of right angled triangle')
print(f'Length of side A: {side_a}')
print(f'Length of side B: {side_b}\n')

sum_squares = side_a ** 2 + side_b ** 2  # Applying formula c^2 = a^2 + b^2

side_c = int(math.sqrt(sum_squares))   # c = Sqrt(a^2 + b^2)

print('Calculating length of side c')
print('-'*35)
print(f'Hypotenuse Length: {side_c}')


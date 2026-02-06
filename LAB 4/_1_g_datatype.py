"""
The "isinstance" function can check the data type of a variable. What does the is_number function do?
Is it possible to improve the code?
"""

def is_number(x):   # It is used to find that the argument passsed is a number integer, decimal
    if isinstance(x, int):
        return True
    elif isinstance(x, float):
        return True
    return False
print("call is_number(5.5),is_number(42)")
print(is_number(5.5))
print(is_number(42))

print("Improvising the function is_number- convert 4 loc to 1 loc")
def is_number_v1(x):
    return isinstance(x, (int,float))
print("call is_number_v1(52.5),is_number_v1(48)")
print(is_number_v1(52.5))
print(is_number_v1(48))

import numbers
print("writing a function using numbers module")
def is_number_v2(x):
    return isinstance(x, numbers.Number)
print("call is_number(5.5),is_number(42))")
print(is_number_v2(5))
print(is_number_v2(42))
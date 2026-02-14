"""
3a Consider the function find_median(numbers), which takes a list of numbers and returns the median.
 The median is the middle number, e.g. the median is 2 for the list [1, 2, 1000]. If the list has an even number of elements, the function should return the average of the two middle numbers. Formulate the requirements and acceptance criteria (AC) that should apply to the function.

"""
def find_median(numbers):
    if not numbers:
        return None
    elif len(numbers) == 1:
        return numbers[0]
    # 1. Sort the list (crucial for median)
    # Using sorted() avoids mutating the original list
    data = sorted(numbers)
    n = len(data)
    mid = n // 2

    # 2. Check if the list length is even or odd
    if n % 2 == 0:
        # Even: Average of the two middle elements
        return (data[mid - 1] + data[mid]) / 2
    else:
        # Odd: The middle element
        return data[mid]
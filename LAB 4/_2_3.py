"""
The following code should stop looping after 5 iterations. Move it into a function and adjust it according to the comment.
end = 5
y = 1
for x in range(1, 100):
y *= 2
# end the loop with an if statement here
print(y)
"""

def iterate_over():
    end = 5
    y = 1
    for x in range(1, 100):
        y *= 2
        if x == end:
            break
    print(y)

iterate_over()


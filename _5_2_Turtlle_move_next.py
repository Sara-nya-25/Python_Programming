"""
Write a function that moves the pen a suitable distance to the right, without drawing.
The idea is that you should be able to combine it with the square function, to draw multiple squares.
Example:
for x in range(5):
t.square()
t.move_next()
"""
import turtle

t = turtle.Turtle()
def draw_square(side, move):
    for _ in range(5):
        for _ in range(4):
            t.color("blue")
            t.forward(side)
            t.left(90)

        t.penup()
        t.forward(side + move)
        t.pendown()



t.speed(1)
side_length = 100
gap = 30
draw_square(side_length, gap)

turtle.exitonclick()
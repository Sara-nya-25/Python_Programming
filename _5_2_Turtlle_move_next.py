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
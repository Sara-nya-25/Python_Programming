import turtle

t = turtle.Turtle()
def draw_square(side):


    for _ in range(4):
        t.color("blue")
        t.forward(side)
        t.left(90)
        t.penup()
        t.pendown()


t.speed(1)

draw_square(100)

turtle.exitonclick()
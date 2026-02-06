import turtle
turtle.resetscreen()
t = turtle.Turtle()
t.speed(0) # Fastest speed
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

for x in range(100):
    t.pencolor(colors[x % 6]) # Cycle through colors
    t.width(x // 100 + 1)     # Get thicker as we go
    t.forward(x)
    t.left(59)                # A slight turn creates the spiral

turtle.done()

import turtle

# 1. Setup the turtle and screen
t = turtle.Turtle()
screen = turtle.Screen()
t.speed(0)  # Makes it faster so you don't get bored!


# 2. The Square Function
def draw_square(side_length):
    for _ in range(4):
        t.forward(side_length)
        t.right(90)


# 3. The Move Next Function (The "Pen Up" trick)
def move_next(distance):
    t.penup()
    t.forward(distance)
    t.pendown()


# 4. The Circle/Polygon Function (using your parameters)
def draw_circle_path(segments, step_length, angle):
    for _ in range(segments):
        t.forward(step_length)
        t.right(angle)


# --- EXECUTION ---
try:
    # Example: Draw 3 squares in a row
    for _ in range(3):
        draw_square(50)
        move_next(70)

    # Example: Move down and draw the circle path
    t.penup()
    t.goto(0, -100)  # Move to a new spot
    t.pendown()
    draw_circle_path(12, 40, 30)  # 12 * 30 = 360 degrees

except turtle.Terminator:
    print("The drawing window was closed early!")

# 5. THE TERMINATOR PREVENTER
# This keeps the window open until you click it.
# Don't put drawing code after this line!
screen.exitonclick()
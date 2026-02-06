"""
Write functions that draw the individual letters of the word "PYTHON" using the turtle module.
Combine them and try to get the letters to be drawn the same size, in a straight line.
"""
import turtle

t = turtle.Turtle()
t.speed(3)
t.pensize(3)

def move_gap():
    """Lifts pen and moves to the start of the next letter."""
    t.penup()
    t.forward(20)
    t.pendown()

def draw_P():
    t.left(90)
    t.forward(100)  # Stem
    t.right(90)
    for _ in range(18): # Curve
        t.forward(5)
        t.right(10)
    t.penup()
    t.goto(t.xcor() + 60, t.ycor() - 100) # Reset to bottom-right
    t.setheading(0)
    t.pendown()

def draw_Y():
    t.penup()
    t.goto(t.xcor() + 30, t.ycor()) # Move to middle
    t.pendown()
    t.left(90)
    t.forward(50)   # Tail
    t.left(30)
    t.forward(60)   # Left branch
    t.backward(60)
    t.right(60)
    t.forward(60)   # Right branch
    t.penup()
    t.goto(t.xcor() + 30, t.ycor() - 100) # Reset to bottom-right
    t.setheading(0)
    t.pendown()

def draw_T():
    t.penup()
    t.forward(30)
    t.pendown()
    t.left(90)
    t.forward(100)  # Stem
    t.left(90)
    t.forward(30)   # Left cross
    t.backward(60)  # Right cross
    t.penup()
    t.goto(t.xcor() + 60, t.ycor() - 100) # Reset to bottom-right
    t.setheading(0)
    t.pendown()

def draw_H():
    t.left(90)
    t.forward(100)  # Left stem
    t.backward(50)
    t.right(90)
    t.forward(60)   # Bridge
    t.left(90)
    t.forward(50)   # Right stem top
    t.backward(100) # Right stem bottom
    t.setheading(0)
    t.pendown()

def draw_O():
    t.penup()
    t.forward(30)
    t.pendown()
    # Draw a circle with a radius of 50
    t.circle(50)
    t.penup()
    t.forward(60)
    t.pendown()

def draw_N():
    t.left(90)
    t.forward(100)  # Left stem
    # Calculate diagonal using Pythagoras or visual estimation
    t.goto(t.xcor() + 60, t.ycor() - 100)
    t.forward(100)  # Right stem
    t.backward(100)
    t.setheading(0)

# --- EXECUTION ---
# Start position
t.penup()
t.goto(-250, 0)
t.pendown()

# Drawing the word
draw_P(); move_gap()
draw_Y(); move_gap()
draw_T(); move_gap()
draw_H(); move_gap()
draw_O(); move_gap()
draw_N()

turtle.done()
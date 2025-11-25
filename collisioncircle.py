import turtle
import time
import math

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Collision of Two Circle Outlines")
time.sleep(0.05)

def make_circle():
    t = turtle.Turtle()
    t.speed(0)
    t.color("white")
    t.penup()
    return t

# Circle turtles
c1 = make_circle()
c2 = make_circle()

# Circle radius
R = 40  # visible outline radius

# Starting positions
c1.goto(-200, -R)
c2.goto(200, -R)

# Draw initial circles
def draw_circle(t):
    t.clear()
    t.pendown()
    t.circle(R)
    t.penup()

draw_circle(c1)
draw_circle(c2)

# Movement speeds
speed1 = 2
speed2 = -2

while True:
    # Update x-positions
    x1 = c1.xcor() + speed1
    x2 = c2.xcor() + speed2

    # Move turtles
    c1.goto(x1, -R)
    c2.goto(x2, -R)

    # Redraw circles at new position
    draw_circle(c1)
    draw_circle(c2)

    # Centers for distance check
    cx1, cy1 = c1.xcor(), 0
    cx2, cy2 = c2.xcor(), 0

    # Distance between centers
    distance = math.dist((cx1, cy1), (cx2, cy2))

    if distance <= (2 * R):
        c1.color("red")
        c2.color("red")
        draw_circle(c1)
        draw_circle(c2)
        break


turtle.done()

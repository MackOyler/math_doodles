import turtle
import math

def hex_snowflake(t, size, depth):
    if depth == 0:
        t.forward(size)
        return

    size /= 3
    hex_snowflake(t, size, depth-1)
    t.left(60)
    hex_snowflake(t, size, depth-1)
    t.right(120)
    hex_snowflake(t, size, depth-1)
    t.left(60)
    hex_snowflake(t, size, depth-1)

# Setup
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

depth = 3
length = 100

for i in range(6):
    hex_snowflake(t, length, depth)
    t.right(60)

screen.mainloop()

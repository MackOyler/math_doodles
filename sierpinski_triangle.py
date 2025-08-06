import turtle

def sierpinski(t, length, depth):
    if depth == 0:
        for _ in range(3):
            t.forward(length)
            t.left(120)
    else:
        sierpinski(t, length/2, depth-1)
        t.forward(length/2)
        sierpinski(t, length/2, depth-1)
        t.backward(length/2)
        t.left(60)
        t.forward(length/2)
        t.right(60)
        sierpinski(t, length/2, depth-1)
        t.left(60)
        t.backward(length/2)
        t.right(60)

# Setup
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-200, -100)
t.pendown()

depth = 4
length = 400
sierpinski(t, length, depth)
screen.mainloop()

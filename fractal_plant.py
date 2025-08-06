import turtle
import random

def apply_rules(axiom, rules, depth):
    for _ in range(depth):
        axiom = "".join(rules.get(c, c) for c in axiom)
    return axiom

def draw_l_system(t, instructions, length, angle):
    stack = []
    for command in instructions:
        if command == 'F':
            t.forward(length)
        elif command == '+':
            t.right(angle)
        elif command == '-':
            t.left(angle)
        elif command == '[':
            stack.append((t.pos(), t.heading()))
        elif command == ']':
            pos, heading = stack.pop()
            t.penup()
            t.setpos(pos)
            t.setheading(heading)
            t.pendown()

# Setup
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.left(90)
t.penup()
t.setpos(0, -250)
t.pendown()

# 🎲 Random parameters
angle = random.uniform(15, 35)
depth = random.randint(3, 5)
length = random.randint(3, 7)
t.pencolor(random.random(), random.random(), random.random())

# Plant-like L-System
axiom = "X"
rules = {
    "X": "F+[[X]-X]-F[-FX]+X",
    "F": "FF"
}

instructions = apply_rules(axiom, rules, depth)
draw_l_system(t, instructions, length, angle)

screen.mainloop()

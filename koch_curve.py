import turtle
import random

def apply_rules(axiom, rules, depth):
    for _ in range(depth):
        axiom = "".join(rules.get(char, char) for char in axiom)
    return axiom

def draw_l_system(t, instructions, length, angle):
    for command in instructions:
        if command == 'F':
            t.forward(length)
        elif command == '+':
            t.right(angle)
        elif command == '-':
            t.left(angle)

# Setup
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

# 🎲 RANDOMIZED PARAMETERS
angle = random.choice([60, 90, 120])
length = random.randint(3, 7)
depth = random.randint(2, 4)

colors = ["red", "green", "blue", "purple", "orange", "cyan"]
t.pencolor(random.choice(colors))

# 🧊 Koch-like pattern (still using standard rule)
axiom = "F"
rules = {"F": "F+F−F−F+F"}

instructions = apply_rules(axiom, rules, depth)
draw_l_system(t, instructions, length, angle)

screen.mainloop()

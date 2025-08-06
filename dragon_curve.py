import turtle

def apply_rules(axiom, rules, depth):
    for _ in range(depth):
        axiom = "".join(rules.get(c, c) for c in axiom)
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

# Dragon Curve
axiom = "FX"
rules = {
    "X": "X+YF+",
    "Y": "-FX-Y"
}
depth = 10
angle = 90
length = 5

instructions = apply_rules(axiom, rules, depth)
instructions = "".join(c for c in instructions if c in "F+-")  # Clean out X/Y
draw_l_system(t, instructions, length, angle)
screen.mainloop()

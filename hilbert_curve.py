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

# Hilbert Curve
axiom = "A"
rules = {
    "A": "+BF-AFA-FB+",
    "B": "-AF+BFB+FA-"
}
depth = 5
angle = 90
length = 10

instructions = apply_rules(axiom, rules, depth)
instructions = "".join(c for c in instructions if c in "F+-")  # Clean out A/B
draw_l_system(t, instructions, length, angle)
screen.mainloop()

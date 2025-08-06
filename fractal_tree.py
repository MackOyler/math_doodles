import turtle

def apply_rules(axiom, rules, depth):
    for _ in range(depth):
        axiom = "".join(rules.get(char, char) for char in axiom)
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
            stack.append((t.position(), t.heading()))
        elif command == ']':
            pos, heading = stack.pop()
            t.penup()
            t.setposition(pos)
            t.setheading(heading)
            t.pendown()

# Setup
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.left(90)  # Point turtle upward
t.penup()
t.setpos(0, -200)
t.pendown()

# L-System: Fractal Tree
axiom = "F"
rules = {
    "F": "FF-[-F+F+F]+[+F-F-F]"
}
depth = 5
angle = 22
length = 5

instructions = apply_rules(axiom, rules, depth)
draw_l_system(t, instructions, length, angle)

screen.mainloop()

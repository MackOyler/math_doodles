# Math Doodles

A collection of fun, fractal-inspired **math-based art programs** using Python’s built-in `turtle` graphics module.

This project is perfect for anyone curious about:
- Fractals
- L-Systems (Lindenmayer Systems)
- Recursive graphics
- Math-inspired generative art
- Playing with simple Python code that creates beautiful visuals

Each `.py` file draws a unique pattern, such as:
- Koch Snowflake
- Fractal Tree
- Dragon Curve
- Hilbert Curve
- Sierpinski Triangle
- Fractal Plant
...and more!

---

## How It Works

### Turtle Graphics

Python’s `turtle` module is a built-in drawing library that lets you control a “turtle” that moves around the screen, drawing lines based on commands like:
- `forward(length)`
- `right(angle)`
- `left(angle)`
- `penup()` / `pendown()`

We use this to simulate drawing on a canvas.

---

### L-Systems (Lindenmayer Systems)

Several of the patterns use **L-systems**, which are simple rule-based systems that generate strings recursively. For example:

Axiom: F
Rule: F → F+F−F−F+F
Depth: 2
Result: F+F−F−F+F + F+F−F−F+F − ...


These strings are interpreted as turtle drawing commands:
- `F` = move forward
- `+` = turn right
- `-` = turn left
- `[` and `]` = push/pop position (used in tree/plant structures)

---

## Requirements

No external libraries needed — just built-in Python modules!

- Python 3.6+
- (Optional) VS Code or any code editor
- Works on macOS, Windows, or Linux

### Check if Python is installed:

```bash
python --version
# or
python3 --version
```

## How to Run It
1. Clone the Repository
```bash
Copy code
git clone https://github.com/MackOyler/math_doodles.git
cd math_doodles
```

2. Run Any Script
Choose a .py file and run it:

```bash
Copy code
python3 koch_curve.py
# or
python3 fractal_tree.py
```

Each script opens a new window and draws a pattern using Turtle.

## Customization
Each script can be easily customized!

## Common parameters you can tweak:
* **angle**: turning angle (e.g., 60, 90)
* **length**: size of line segments
* **depth**: recursion level (higher = more detail)
* **rules**: L-system rules (dict)
* **axiom**: starting symbol
* **colors**: use t.pencolor() to change drawing color

## Learn More
* [Lindenmayer System (Wikipedia)](https://en.wikipedia.org/wiki/L-system)
* [Turtle Graphics in Python Docs](https://docs.python.org/3/library/turtle.html)
* [Fractals with L-Systems](https://www.youtube.com/watch?v=J0LyZSgVKVc)

## Created for fun by Mack Oyler
If you found this interesting or educational, feel free to star the repo or fork it and try your own experiments!
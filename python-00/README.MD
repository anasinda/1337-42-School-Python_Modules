# Python00 — Growing Code: Python Fundamentals Through Garden Data

[![1337](https://img.shields.io/badge/1337-000000?style=for-the-badge&logoColor=white)](https://www.1337.ma/)
[![UM6P](https://img.shields.io/badge/UM6P-C1392B?style=for-the-badge)](https://um6p.ma/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Beginner](https://img.shields.io/badge/Level-Beginner-2ecc71?style=for-the-badge)](https://python.org)

The first module in the Python Learning Modules series — discover Python's fundamental syntax and semantics through analyzing community garden data. Learn expressions, variables, functions, and control flow while contributing to sustainable community initiatives.

— Why this module matters

- **Foundational skills** — start your Python journey with the building blocks of programming
- **Real-world context** — garden data makes abstract concepts tangible and meaningful
- **Progressive difficulty** — each exercise builds on previous concepts
- **Community focus** — learn programming while solving real community garden challenges

--------------------------------------------------------------------------------

## Quick highlights

- **8 hands-on exercises** — from "Hello Garden" to seed inventory management
- **Core concepts** — variables, functions, conditionals, loops, recursion, type hints
- **Beginner-friendly** — no prior Python knowledge required
- **Practical focus** — each exercise solves a real garden management problem
- **Clean code practices** — introduction to type hints and function design

--------------------------------------------------------------------------------

## Module structure

```
Python00/
├── ex0/                          # Exercise 0: Hello Garden
│   └── ft_hello_garden.py       # First function — display welcome message
├── ex1/                          # Exercise 1: Garden Plot Area
│   └── ft_plot_area.py          # Calculate rectangular plot area
├── ex2/                          # Exercise 2: Harvest Total
│   └── ft_harvest_total.py      # Sum multiple harvest numbers
├── ex3/                          # Exercise 3: Plant Age Check
│   └── ft_plant_age.py          # Conditional logic for harvest readiness
├── ex4/                          # Exercise 4: Water Reminder
│   └── ft_water_reminder.py     # Decision-making with if/else
├── ex5/                          # Exercise 5: Count to Harvest
│   ├── ft_count_harvest_iterative.py  # Loops (iteration)
│   └── ft_count_harvest_recursive.py  # Recursion basics
├── ex6/                          # Exercise 6: Garden Summary
│   └── ft_garden_summary.py     # Combine multiple pieces of data
├── ex7/                          # Exercise 7: Seed Inventory
│   └── ft_seed_inventory.py     # Type hints and string methods
├── __init__.py                   # Package initialization
└── README.md                     # You are here
```

--------------------------------------------------------------------------------

## Exercise details — what you'll build

### Exercise 0: `ft_hello_garden.py`
*Your first Python function*

```python
>>> ft_hello_garden()
Hello, Garden Community!
```

**Concepts:** Function definition, `print()`, basic output

---

### Exercise 1: `ft_plot_area.py`
*Calculate garden plot dimensions*

```python
>>> ft_plot_area()
Enter length: 5
Enter width: 3
Plot area: 15
```

**Concepts:** `input()`, type conversion (`int()`), arithmetic, variables

---

### Exercise 2: `ft_harvest_total.py`
*Sum multiple harvest numbers*

```python
>>> ft_harvest_total()
Enter harvest count 1: 12
Enter harvest count 2: 8
Enter harvest count 3: 15
Total harvest: 35
```

**Concepts:** Multiple inputs, accumulation, `int()` conversion

---

### Exercise 3: `ft_plant_age.py`
*Check if plants are ready to harvest*

```python
>>> ft_plant_age()
Enter plant age in days: 75
Plant is ready to harvest!

>>> ft_plant_age()
Enter plant age in days: 45
Plant needs more time to grow.
```

**Concepts:** Conditionals (`if/else`), comparison operators

---

### Exercise 4: `ft_water_reminder.py`
*Smart watering reminders*

```python
>>> ft_water_reminder()
Days since last watering: 4
Water the plants!

>>> ft_water_reminder()
Days since last watering: 1
Plants are fine
```

**Concepts:** Decision-making, boolean logic, user input validation

---

### Exercise 5: Two approaches to counting

**Iterative:** `ft_count_harvest_iterative.py`
```python
>>> ft_count_harvest_iterative()
Days until harvest: 5
Day 1
Day 2
Day 3
Day 4
Day 5
Harvest time!
```

**Recursive:** `ft_count_harvest_recursive.py`
```python
>>> ft_count_harvest_recursive()
Days until harvest: 5
Day 1
Day 2
Day 3
Day 4
Day 5
Harvest time!
```

**Concepts:** Loops (`for`/`range`), recursion, function call stack

---

### Exercise 6: `ft_garden_summary.py`
*Create a garden information summary*

```python
>>> ft_garden_summary()
Enter garden name: Community Garden
Enter number of plants: 25
Garden: Community Garden
Plants: 25
Status: Growing well!
```

**Concepts:** String formatting, combining multiple data sources, fixed messages

---

### Exercise 7: `ft_seed_inventory.py`
*Track seed packets with type hints*

```python
>>> ft_seed_inventory("tomato", 15, "packets")
Tomato seeds: 15 packets available

>>> ft_seed_inventory("carrot", 8, "grams")
Carrot seeds: 8 grams total

>>> ft_seed_inventory("lettuce", 12, "area")
Lettuce seeds: covers 12 square meters

>>> ft_seed_inventory("basil", 5, "invalid")
Unknown unit type
```

**Concepts:** Type hints (`str`, `int`, `-> None`), string methods (capitalization), conditional logic, function parameters

Function signature:
```python
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
```

--------------------------------------------------------------------------------

## Key concepts mastered

| Concept | Exercises | Why it matters |
|---------|-----------|----------------|
| **Functions** | All exercises | Building reusable code blocks |
| **Variables** | Ex1-7 | Storing and manipulating data |
| **Input/Output** | Ex0-6 | User interaction |
| **Type conversion** | Ex1-5 | `int()`, `str()` — handling user input |
| **Conditionals** | Ex3, Ex4, Ex7 | Program decision-making |
| **Loops** | Ex5 (iterative) | Repetition and iteration |
| **Recursion** | Ex5 (recursive) | Functions calling themselves |
| **String methods** | Ex7 | `.capitalize()` for clean output |
| **Type hints** | Ex7 | Modern Python best practices |

--------------------------------------------------------------------------------

## Getting started

### Prerequisites

- Python 3.10 or later
- A text editor or IDE
- Basic command line knowledge

### Installation

```bash
# Navigate to the Python00 module
cd python-learning-modules/Python00

# No additional dependencies required — pure Python!
```

### Running exercises

Each exercise is a standalone Python file:

```bash
# Run Exercise 0
python3 ex0/ft_hello_garden.py

# Run Exercise 1
python3 ex1/ft_plot_area.py

# ... and so on
```

### Using the helper tool

The module includes a testing helper (`main.py` in the original project) that can import and test your functions automatically:

```bash
# Copy the helper to your working directory
cp /path/to/main.py .

# Run the helper
python3 main.py
```

The helper will guide you through testing each exercise.

--------------------------------------------------------------------------------

## Exercise guidelines

### What to submit

Each exercise file should contain **only** the requested function — no `if __name__ == "__main__":` blocks, no test calls.

**Correct:**
```python
def ft_plot_area():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    print(f"Plot area: {length * width}")
```

**Incorrect:**
```python
def ft_plot_area():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    print(f"Plot area: {length * width}")

# Don't include this!
if __name__ == "__main__":
    ft_plot_area()
```

### Authorized functions

Each exercise specifies exactly what you're allowed to use:

| Exercise | Authorized |
|----------|------------|
| Ex0 | `print()` |
| Ex1-4 | `input()`, `int()`, `print()` |
| Ex5 | `input()`, `int()`, `print()`, `range()` |
| Ex6 | `input()`, `print()` |
| Ex7 | `print()` |

### Error handling

For this introductory module, you don't need to handle invalid inputs (negative numbers, letters where numbers are expected). The behavior is **undefined** — focus on the happy path.

--------------------------------------------------------------------------------

## Learning path — where this module fits

```
Python00 (Fundamentals) ◀── You are here
    ↓
Python01 (OOP Basics)
    ↓
Python-02 (Error Handling)
    ↓
Python-03 (Collections)
    ↓
... and beyond
```

Master these fundamentals before moving to more advanced modules. Each concept in Python00 is essential for everything that follows.

--------------------------------------------------------------------------------

## Common questions

### Why no error handling?
This module focuses on basic syntax and logic. Error handling is introduced in Python-02 (Garden Guardian) after you've mastered the fundamentals.

### Why only functions, not full programs?
Each exercise isolates a single concept. The `main.py` helper handles program execution, letting you focus on writing correct functions.

### What's with the "ft_" prefix?
"ft_" stands for "function" — it's a naming convention to clearly identify exercise files.

### Do I need to understand recursion for Exercise 5?
Both iterative and recursive versions are required, but the recursive version is intentionally simple. It's your first exposure to recursion — you'll see it again in later modules.

--------------------------------------------------------------------------------

## Resources

- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Type Hints Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
- [Think Python: How to Think Like a Computer Scientist](https://greenteapress.com/thinkpython2/html/index.html)

--------------------------------------------------------------------------------

## Contributing & contact

Found a bug? Have a suggestion? Open an issue or reach out to `anasinda`.

---

## License

MIT License — see `LICENSE` file at repository root.

---

*"In community gardens across the world, data tells stories of growth, collaboration, and impact. Python, like these gardens, grows from simple seeds into something powerful and nourishing."*

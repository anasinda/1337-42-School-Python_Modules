# Python01 — CodeCultivation: Object-Oriented Garden Systems

[![1337](https://img.shields.io/badge/1337-000000?style=for-the-badge&logoColor=white)](https://www.1337.ma/)
[![UM6P](https://img.shields.io/badge/UM6P-C1392B?style=for-the-badge)](https://um6p.ma/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Intermediate](https://img.shields.io/badge/Level-Intermediate-f39c12?style=for-the-badge)](https://python.org)

The second module in the Python Learning Modules series — build a comprehensive digital garden ecosystem while mastering Object-Oriented Programming. Design classes, model real-world relationships through inheritance, and architect scalable systems while managing a community garden.

— Why this module matters

- **OOP fundamentals** — move from writing scripts to designing systems with classes, instances, and methods
- **Progressive architecture** — each exercise builds directly on the last, culminating in a full analytics platform
- **Real encapsulation** — learn why protecting data matters and how to enforce it with controlled access
- **Inheritance chains** — model real-world relationships between plant types through class hierarchies
- **Clean code practices** — docstrings, type hints, `@staticmethod`, `@classmethod`, and flake8 compliance throughout

--------------------------------------------------------------------------------

## Quick highlights

- **7 hands-on exercises** — from "Hello Garden" to a multi-manager analytics platform
- **Core concepts** — classes, `__init__`, instance/class variables, encapsulation, inheritance, `super()`, `@staticmethod`, `@classmethod`, nested classes
- **Intermediate level** — builds directly on Python00 fundamentals
- **Practical focus** — each exercise solves a real garden management problem through OOP design
- **Clean code practices** — introduction to method types, access control conventions, and class design patterns

--------------------------------------------------------------------------------

## Module structure

```
Python01/
├── ex0/                          # Exercise 0: Planting Your First Seed
│   └── ft_garden_intro.py       # Program entry point — if __name__ == "__main__"
├── ex1/                          # Exercise 1: Garden Data Organizer
│   └── ft_garden_data.py        # First class — Plant blueprint with attributes
├── ex2/                          # Exercise 2: Plant Growth Simulator
│   └── ft_plant_growth.py       # Instance methods — grow(), age(), get_info()
├── ex3/                          # Exercise 3: Plant Factory
│   └── ft_plant_factory.py      # Class variables — tracking instances with count
├── ex4/                          # Exercise 4: Garden Security System
│   └── ft_garden_security.py    # Encapsulation — protected attributes, getters/setters
├── ex5/                          # Exercise 5: Specialized Plant Types
│   └── ft_plant_types.py        # Inheritance — Flower, Tree, Vegetable from Plant
├── ex6/                          # Exercise 6: Garden Analytics Platform
│   └── ft_garden_analytics.py   # Full system — classmethods, staticmethods, nested classes
├── __init__.py                   # Package initialization
└── README.md                     # You are here
```

--------------------------------------------------------------------------------

## Exercise details — what you'll build

### Exercise 0: `ft_garden_intro.py`
*Your first structured Python program*

```python
$> python3 ft_garden_intro.py
=== Welcome to My Garden ===
Plant: Rose
Height: 25cm
Age: 30 days

=== End of Program ===
```

**Concepts:** Program entry point, `if __name__ == "__main__"`, variables, `print()`

---

### Exercise 1: `ft_garden_data.py`
*Organize plant data with a class blueprint*

```python
$> python3 ft_garden_data.py
=== Garden Plant Registry ===
Rose: 25cm, 30 days old
Sunflower: 80cm, 45 days old
Cactus: 15cm, 120 days old
```

**Concepts:** `class`, `__init__`, instance attributes, instance methods, `self`

---

### Exercise 2: `ft_plant_growth.py`
*Simulate plant growth over time*

```python
$> python3 ft_plant_growth.py
=== Day 1 ===
Rose: 25cm, 30 days old
=== Day 7 ===
Rose: 31cm, 36 days old
Growth this week: +6cm
```

**Concepts:** Instance methods that modify state (`grow()`, `age()`), method return values, simulation loops

---

### Exercise 3: `ft_plant_factory.py`
*Track how many plants have been created*

```python
$> python3 ft_plant_factory.py
=== Plant Factory Output ===
Created: Rose (25cm, 30 days)
Created: Oak (200cm, 365 days)
Created: Cactus (5cm, 90 days)
Created: Sunflower (80cm, 45 days)
Created: Fern (15cm, 120 days)

Total plants created: 5
```

**Concepts:** Class variables vs instance variables, shared state across instances, static-style methods

---

### Exercise 4: `ft_garden_security.py`
*Protect plant data from corruption*

```python
$> python3 ft_garden_security.py
=== Garden Security System ===
Plant created: Rose
Height updated: 25cm [OK]
Age updated: 30 days [OK]

Invalid operation attempted: height -5cm [REJECTED]
Security: Negative height rejected

Current plant: Rose (25cm, 30 days)
```

**Concepts:** Encapsulation, protected attributes (`_name`), custom getters/setters, data validation, access control conventions

---

### Exercise 5: `ft_plant_types.py`
*Model a family tree of plant types*

```python
$> python3 ft_plant_types.py
=== Garden Plant Types ===

Rose (Flower): 25cm, 30 days, red color
Rose is blooming beautifully!

Oak (Tree): 500cm, 1825 days, 50cm diameter
Oak provides 78 square meters of shade

Tomato (Vegetable): 80cm, 90 days, summer harvest
Tomato is rich in vitamin C
```

**Concepts:** Inheritance, `super().__init__()`, method overriding, specialized subclasses (`Flower`, `Tree`, `Vegetable`), avoiding code duplication

Class signatures:
```python
class Plant:
    def __init__(self, name: str, plant_type: str, height_cm: int, age_days: int) -> None:

class Flower(Plant):
    def __init__(self, name: str, plant_type: str, height_cm: int, age_days: int, flower_color: str) -> None:

class Tree(Plant):
    def __init__(self, name: str, plant_type: str, height_cm: int, age_days: int, trunk_diameter: int) -> None:

class Vegetable(Plant):
    def __init__(self, name: str, plant_type: str, height_cm: int, age_days: int, harvest_season: str, nut_value: str) -> None:
```

---

### Exercise 6: `ft_garden_analytics.py`
*Build a full garden management and analytics platform*

```python
$> python3 ft_garden_analytics.py
=== Garden Management System Demo ===

Added Oak Tree to Alice's Garden
Added Rose to Alice's Garden
Added Sunflower to Alice's Garden

Alice is helping all plants grow...
Oak Tree grew 1cm
Rose grew 1cm
Sunflower grew 1cm

===Alice's Garden Report
Plants in garden:
- Oak Tree: 101cm
- Rose: 26cm, red flowers (blooming)
- Sunflower: 51cm, yellow flowers (blooming), Prize points: 10

Plants added: 3, Total growth: 3cm
Plant types: 1 regular, 1 flowering, 1, prize flowers

Height validation test: True
Garden scores - Alice: 218, Bob: 92
Total gardens managed: 2
```

**Concepts:** `@classmethod`, `@staticmethod`, nested classes (`GardenStats` inside `GardenManager`), inheritance chain (`Plant → FloweringPlant → PrizeFlower`), `isinstance()`, factory pattern via `create_garden_network()`

--------------------------------------------------------------------------------

## Key concepts mastered

| Concept | Exercises | Why it matters |
|---------|-----------|----------------|
| **Classes & instances** | Ex1–6 | Modeling real-world objects as blueprints |
| **`__init__` & `self`** | Ex1–6 | Setting up object state at creation |
| **Instance methods** | Ex2–6 | Giving objects behaviors they perform on themselves |
| **Class variables** | Ex3 | Tracking shared state across all instances |
| **Encapsulation** | Ex4 | Protecting data integrity with controlled access |
| **Inheritance** | Ex5–6 | Reusing and extending behavior across related classes |
| **`super()`** | Ex5–6 | Delegating initialization up the class hierarchy |
| **`@classmethod`** | Ex6 | Methods that operate on the class itself, not instances |
| **`@staticmethod`** | Ex6 | Utility functions logically grouped inside a class |
| **Nested classes** | Ex6 | Organizing helper components inside their owner class |

--------------------------------------------------------------------------------

## Getting started

### Prerequisites

- Python 3.10 or later
- Completion of Python00 (Fundamentals) or equivalent knowledge
- A text editor or IDE
- Basic command line knowledge

### Installation

```bash
# Navigate to the Python01 module
cd python-learning-modules/Python01

# No additional dependencies required — pure Python!
```

### Running exercises

Each exercise is a standalone Python file:

```bash
# Run Exercise 0
python3 ex0/ft_garden_intro.py

# Run Exercise 1
python3 ex1/ft_garden_data.py

# ... and so on
```

--------------------------------------------------------------------------------

## Exercise guidelines

### What to submit

Each exercise file should contain the requested class definitions and any required demonstration code. You may include test code inside an `if __name__ == "__main__":` block.

**Correct:**
```python
class Plant:
    def __init__(self, name: str, height_cm: int, age_days: int):
        """Setting up plant attributes."""
        self.name = name
        self.height = height_cm
        self.age = age_days

    def get_stats(self) -> None:
        """Get info about plant."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    rose.get_stats()
```

**Incorrect:**
```python
class Plant:
    def __init__(self, name, height_cm, age_days):  # Missing type hints
        self.name = name                             # Missing docstring
        self.height = height_cm
        self.age = age_days

rose = Plant("Rose", 25, 30)  # Test code outside __main__ guard
print(rose.name)
```

### Authorized tools per exercise

| Exercise | Authorized |
|----------|------------|
| Ex0 | `print()`, `if __name__ == "__main__"` |
| Ex1 | `class`, `__init__`, `print()` |
| Ex2 | `class`, `__init__`, `print()` |
| Ex3 | `class`, `__init__`, `print()` |
| Ex4 | `class`, `__init__`, `def`, `print()`, setter/getter (custom) |
| Ex5 | `class`, `__init__`, `super()`, `print()` |
| Ex6 | `class`, `__init__`, `super()`, `print()`, `staticmethod()`, `classmethod()` |

### Code standards

All submitted code must follow **flake8** linting standards:

- Max line length: 79 characters
- Classes in `PascalCase`, functions and variables in `snake_case`
- Docstrings required on all classes, methods, and functions
- Type hints encouraged on all function signatures

--------------------------------------------------------------------------------

## Learning path — where this module fits

```
Python00 (Fundamentals)
    ↓
Python01 (OOP Basics) ◀── You are here
    ↓
Python-02 (Error Handling)
    ↓
Python-03 (Collections)
    ↓
... and beyond
```

Completing this module gives you the OOP foundation that every subsequent module depends on. Classes, inheritance, and encapsulation will appear in every project from here forward.

--------------------------------------------------------------------------------

## Common questions

### Why use `_` (single underscore) for protected attributes?
The single underscore is Python's convention for "internal use" — it signals to other developers that an attribute shouldn't be accessed directly. It doesn't enforce access at the language level, but it communicates intent clearly. True private attributes use double underscores (`__`), covered in later modules.

### What's the difference between `@staticmethod` and `@classmethod`?
A `@staticmethod` is a plain function that lives inside a class for organizational reasons — it receives no automatic first argument. A `@classmethod` receives the class itself as its first argument (`cls`), which lets it create or modify class-level state. Use `@classmethod` when the method needs to know about the class; use `@staticmethod` when it's just a utility that belongs conceptually to the class.

### Why nest `GardenStats` inside `GardenManager`?
Nesting keeps the stats helper logically tied to the manager that uses it. It prevents `GardenStats` from being used out of context and communicates that it's an implementation detail of `GardenManager`, not a standalone public class.

### What's with the `"ft_"` prefix?
`"ft_"` stands for "function/file" — it's a naming convention used across the 42 curriculum to clearly identify exercise submission files.

### Do I need to handle invalid inputs?
Only where explicitly mentioned (Exercise 4 — the security system). All other exercises assume valid input. Focus on demonstrating the OOP concept clearly.

--------------------------------------------------------------------------------

## Resources

- [Official Python Tutorial — Classes](https://docs.python.org/3/tutorial/classes.html)
- [Python `super()` explained](https://docs.python.org/3/library/functions.html#super)
- [Real Python — OOP in Python](https://realpython.com/python3-object-oriented-programming/)
- [Type Hints Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
- [flake8 — Python linting tool](https://flake8.pycqa.org/en/latest/)

--------------------------------------------------------------------------------

## Contributing & contact

Found a bug? Have a suggestion? Open an issue or reach out to `anasinda`.

---

## License

MIT License — see `LICENSE` file at repository root.

---

*"Behind every thriving community garden lies a network of relationships. Plants don't grow in isolation — and neither does good code. Well-designed systems emerge when every component has its proper place and purpose."*

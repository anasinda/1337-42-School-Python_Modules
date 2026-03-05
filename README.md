# Python Learning Modules — mastering Python through themed projects, one module at a time

[![1337](https://img.shields.io/badge/1337-000000?style=for-the-badge&logoColor=white)](https://www.1337.ma/)
[![UM6P](https://img.shields.io/badge/UM6P-C1392B?style=for-the-badge)](https://um6p.ma/)
[![42 Badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org) [![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/) [![Poetry](https://img.shields.io/badge/Poetry-60A5FA?style=for-the-badge&logo=poetry&logoColor=white)](https://python-poetry.org/) [![Virtualenv](https://img.shields.io/badge/Virtualenv-ECD53F?style=for-the-badge&logo=python&logoColor=black)](https://virtualenv.pypa.io/)

A comprehensive collection of 11 progressive Python modules designed to take you from fundamentals to advanced programming concepts through engaging, real-world scenarios.

— Why this repository matters

- **Progressive learning path** — each module builds on previous concepts
- **Themed exercises** — garden analytics, space data, card games, and more
- **Real-world patterns** — OOP, error handling, polymorphism, decorators, and abstract classes
- **Modern Python** — type hints, Pydantic v2, virtual environments, and packaging

--------------------------------------------------------------------------------

## Quick highlights

- **11 progressive modules** — from Python fundamentals to advanced patterns
- **55+ hands-on exercises** — progressive coding challenges with clear objectives
- **Real-world themes** — community gardens, space stations, card games, data pipelines
- **Modern tooling** — virtual environments, Poetry, Pydantic, type hints
- **Clean architecture** — abstract classes, interfaces, and design patterns

--------------------------------------------------------------------------------

## Modules overview

| Module | Theme | Concepts |
|--------|-------|----------|
| **Python00** | Growing Code | Fundamentals, functions, control flow, basic I/O |
| **Python01** | Code Cultivation | OOP basics, classes, inheritance, encapsulation |
| **Python-02** | Garden Guardian | Error handling, exceptions, try/except/finally |
| **Python-03** | Data Quest | Collections: lists, tuples, sets, dicts, generators, comprehensions |
| **Python-04** | Cyber Archives | File I/O, context managers, streams, error handling |
| **Python-05** | Code Nexus | Polymorphism, method overriding, inheritance hierarchies |
| **python-06** | The Codex | Imports, packages, `__init__.py`, circular dependencies |
| **Python-07** | DataDeck | Abstract classes, ABC, multiple inheritance, interfaces |
| **python-08** | The Matrix | Virtual environments, pip, Poetry, environment variables |
| **Python-09** | Cosmic Data | Pydantic models, validation, nested structures |
| **Python-10** | FuncMage | Functional programming, lambdas, decorators, closures |

--------------------------------------------------------------------------------

## Project structure

```
python-learning-modules/
├── Python00/           # Growing Code — fundamentals
├── Python01/           # Code Cultivation — OOP basics
├── Python-02/          # Garden Guardian — error handling
├── Python-03/          # Data Quest — collections
├── Python-04/          # Cyber Archives — file I/O
├── Python-05/          # Code Nexus — polymorphism
├── python-06/          # The Codex — imports & packages
├── Python-07/          # DataDeck — abstract classes
├── python-08/          # The Matrix — virtual environments
├── Python-09/          # Cosmic Data — Pydantic
├── Python-10/          # FuncMage — functional programming
├── tools/              # Data generators and helpers
├── LICENSE             # MIT License
└── README.md           # You are here
```

Each module follows a consistent structure:
```
PythonXX/
├── ex0/                # Exercise 0
│   └── ft_exercise.py  # Exercise implementation
├── ex1/
│   └── ...
├── __init__.py         # Package initialization
└── README.md           # Module-specific README
```

--------------------------------------------------------------------------------

## Module details — what you'll learn

### Python00 — Growing Code
*Fundamentals of Python programming through community garden data*
- Variables, expressions, and basic I/O
- Functions and control flow
- Working with numbers and strings
- Simple data validation
- **Exercises:** ~8

### Python01 — Code Cultivation
*Object-oriented programming for garden management*
- Classes and objects
- Inheritance and polymorphism basics
- Encapsulation and data protection
- Building reusable components
- **Exercises:** ~7

### Python-02 — Garden Guardian
*Error handling for resilient data pipelines*
- Try/except blocks and exception types
- Custom exception classes
- Finally blocks and cleanup
- Raising errors and validation
- **Exercises:** ~6

### Python-03 — Data Quest
*Mastering Python collections through game analytics*
- Lists for sequential data
- Tuples for immutable coordinates
- Sets for unique achievements
- Dictionaries for inventory systems
- Generators for memory-efficient streams
- Comprehensions for elegant transformations
- **Exercises:** ~7

### Python-04 — Cyber Archives
*File operations and resource management*
- Reading and writing files
- Context managers (`with` statement)
- Standard streams (stdin, stdout, stderr)
- Error handling for file operations
- Resource cleanup and security
- **Exercises:** ~5

### Python-05 — Code Nexus
*Polymorphism and method overriding*
- Abstract base classes
- Method overriding and `super()`
- Subtype polymorphism
- Building extensible data pipelines
- **Exercises:** ~3

### python-06 — The Codex
*Python's import system and package management*
- `__init__.py` and package initialization
- Absolute vs relative imports
- Circular dependency resolution
- Module organization
- **Exercises:** ~4

### Python-07 — DataDeck
*Abstract classes and interfaces*
- ABC and abstract methods
- Multiple inheritance
- Interface design patterns
- Building flexible game architectures
- **Exercises:** ~5

### python-08 — The Matrix
*Virtual environments and dependency management*
- venv and virtual environments
- pip vs Poetry
- requirements.txt and pyproject.toml
- Environment variables and `.env` files
- **Exercises:** ~3

### Python-09 — Cosmic Data
*Pydantic for data validation*
- BaseModel and Field constraints
- Custom validators (`@model_validator`)
- Nested models and complex structures
- Enum types and validation rules
- **Exercises:** ~3

### Python-10 — FuncMage
*Functional programming patterns*
- Lambda expressions
- Higher-order functions
- Closures and lexical scoping
- Functools (reduce, partial, lru_cache)
- Decorators and `@wraps`
- **Exercises:** ~5

--------------------------------------------------------------------------------

## Getting started

### Prerequisites

- Python 3.10 or later
- pip package manager
- (Optional) Poetry for dependency management

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/python-learning-modules.git
cd python-learning-modules

# (Optional) Create a virtual environment for testing
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install tools dependencies if needed
pip install -r tools/requirements.txt
```

### Working with a module

Each module is self-contained. Navigate to any module and start coding:

```bash
cd Python03  # Data Quest module
ls ex0/      # See available exercises
```

Most exercises can be run directly:

```bash
python3 ex0/ft_command_quest.py arg1 arg2
```

### Using the testing tools

The `tools/` directory contains data generators to help test your implementations:

```bash
cd tools/
python3 data_generator.py  # Generate test data for exercises
```

--------------------------------------------------------------------------------

## Module map — suggested learning path

```
Python00 (Fundamentals) [~8 ex]
    ↓
Python01 (OOP Basics) [~7 ex]
    ↓
Python-02 (Error Handling) [~6 ex]
    ↓
Python-03 (Collections) [~7 ex]
    ↓
Python-04 (File I/O) [~5 ex]
    ↓
Python-05 (Polymorphism) [~3 ex]
    ↓
python-06 (Imports) [~4 ex]
    ↓
Python-07 (Abstract Classes) [~5 ex]
    ↓
python-08 (Virtual Env) [~3 ex]
    ↓
Python-09 (Pydantic) [~3 ex]
    ↓
Python-10 (Functional) [~5 ex]
```

**Total exercises: ~55+**

Each module assumes mastery of previous concepts. Start with Python00 and progress sequentially for the best learning experience.

--------------------------------------------------------------------------------

## Key learning outcomes

- Write clean, maintainable Python code with proper organization
- Understand and apply object-oriented design principles
- Build resilient systems with comprehensive error handling
- Master Python's collection types for efficient data processing
- Create reusable packages with proper import structures
- Implement design patterns using abstract classes and interfaces
- Manage project dependencies with modern tooling
- Validate data with Pydantic models
- Write elegant functional-style code with lambdas and decorators

--------------------------------------------------------------------------------

## Tools & technologies

| Category | Tools |
|----------|-------|
| **Core** | Python 3.10+, type hints, ABC, dataclasses |
| **Validation** | Pydantic v2, custom validators, Field constraints |
| **Packaging** | pip, Poetry, virtualenv, requirements.txt |
| **Functional** | functools, itertools, operator, decorators |
| **Testing** | Built-in generators, custom test helpers |
| **Style** | flake8, PEP 8, docstrings |

--------------------------------------------------------------------------------

## Exercise format

Each exercise follows a consistent pattern:

- **Single function per file** — focused learning objectives
- **Clear specifications** — exact requirements and expected output
- **Authorized imports** — learn constraints like real-world coding
- **Error handling** — graceful failure handling
- **Type hints** — modern Python best practices

Example exercise structure:
```python
def ft_function_name(param: str) -> str:
    """
    Brief description of what the function does.
    
    Args:
        param: Description of parameter
        
    Returns:
        Description of return value
    """
    # Implementation here
    return result
```

--------------------------------------------------------------------------------

## Contributing & contact

Suggestions, bug reports, or improvements are welcome — open an issue or reach out to `anasinda`.

---

## License

MIT License — see `LICENSE` file at repository root.

---

*"Programming, like gardening, is about nurturing growth — both in code and in the communities we serve."*

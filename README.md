# Quantitative Finance Journey

A comprehensive learning repository documenting my journey through quantitative finance, programming fundamentals, and financial analysis.

## 📚 Course Progress

### CS50P - Introduction to Programming with Python

#### Day 1 - Programming Fundamentals
- **Conditionals**: Control flow and decision-making logic
- **Functions**: Code organization and reusability
  - `greet.py` - Basic greeting functions
  - `guess.py` - Number guessing game implementation
  - `machine.py` - Interactive machine simulation
  - `shows.py` - Data handling and display functions
- **Introduction to Programming**: Core programming concepts
- **Loops**: Iteration and repetitive operations
- **Problem Sets**: Practical coding exercises

#### Day 2 - Error Handling
- **Exceptions**: Error handling and debugging techniques
  - `debug.py` - Pyramid drawing with input validation (completed)

### CS50W - Web Programming
- **Day -1**: Initial setup and preparation

### Python for Finance

#### Introduction
- **Notebook 1**: `intro to python for finance.ipynb` - Fundamentals of Python in financial contexts
- **Notebook 2**: Advanced concepts and applications

#### Stock Analysis
- Stock market data analysis and modeling

## 🎯 Learning Objectives

- Master Python programming fundamentals
- Develop quantitative finance skills
- Build web applications for financial data
- Create data analysis and visualization tools
- Implement algorithmic trading strategies

## 🛠️ Technologies & Tools

- **Python**: Core programming language
- **Jupyter Notebooks**: Interactive development environment
- **Financial Libraries**: NumPy, Pandas, Matplotlib (planned)
- **Web Development**: HTML, CSS, JavaScript (CS50W)

## 📈 Progress Tracking

- ✅ CS50P Day 1: Functions, Conditionals, Loops
- ✅ CS50P Day 2: Exception Handling (Basic implementation completed)
- 📋 CS50W: Web Programming (Planned)
- 🔄 Python for Finance: Introduction (In Progress)

## 🚀 Next Steps

1. Enhance exception handling with try-catch blocks and input validation
2. Advance to CS50P data structures and algorithms
3. Begin CS50W web development modules
4. Implement first quantitative finance project
5. Explore financial data APIs and real-time analysis

## 💡 Code Quality Enhancements

### Current Recommendations:
- **Exception Handling**: Add try-catch blocks to handle invalid input in `debug.py`
- **Input Validation**: Implement bounds checking for pyramid height
- **Documentation**: Add docstrings to functions for better code maintainability
- **Type Hints**: Consider adding type annotations for better code clarity
- **Testing**: Create unit tests for core functions
- **Code Organization**: Implement consistent naming conventions across all modules

### Suggested Improvements for `debug.py`:
```python
def main():
    try:
        height = int(input("Height: "))
        if height <= 0:
            raise ValueError("Height must be positive")
        pyramid(height)
    except ValueError as e:
        print(f"Error: {e}")
        return main()  # Retry on invalid input

def pyramid(n: int) -> None:
    """Draw a pyramid of given height using # characters."""
    for i in range(n):
        print("#" * (i + 1))
```

---

*This repository serves as both a learning log and a portfolio of quantitative finance and programming skills development.*

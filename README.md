# Basic Math Calculator

A beginner-level, command-line math calculator project built for a first-year university Python Essentials course.

---

## 1. Project Description

**Basic Math Calculator** is a modular Python command-line application that allows users to perform standard mathematical calculations interactively. It supports seven core arithmetic operations, handles division-by-zero safely without exceptions, records calculation history, tracks unique operations used, and calculates session statistics using only Python's built-in features and standard library.

---

## 2. Features

* **Seven Core Operations**:
  1. Addition (`+`)
  2. Subtraction (`-`)
  3. Multiplication (`*`)
  4. Division (`/`)
  5. Floor Division (`//`)
  6. Modulus (`%`)
  7. Power / Exponentiation (`**`)
* **Safe Division Handling**: Checks for zero divisors using simple conditional statements (`if/else`) without `try/except`.
* **Robust Input Validation**: Validates integer and decimal inputs using pure string inspection and character checking.
* **Calculation History**: Stores completed calculations as immutable tuples within a list.
* **Numerical Results Array**: Uses Python's standard `array` module (`array('d')`) to store numerical results and compute the session average.
* **Bitwise Parity Detection**: Examines whole-number results using the bitwise AND operator (`& 1`) to determine whether the result is even or odd.
* **Unique Operation Tracking**: Uses a `set` to track distinct operators utilized during the session.
* **Session Report on Exit**: Displays a complete history log and summary statistics when the user exits.

---

## 3. Python Concepts Used

This project demonstrates foundational concepts taught in a first-year Python course:

1. **Python Fundamentals**: Indentation, comments, clean naming, and `if __name__ == '__main__':` main guard.
2. **Input and Output Operations**: `input()` for reading user selections and operands; formatted `print()` statements for output.
3. **Variables**: Meaningful, beginner-level variables (`num1`, `num2`, `choice`, `result`, `total_sum`).
4. **Arithmetic Operators**: `+`, `-`, `*`, `/`, `//`, `%`, `**`.
5. **Assignment Operators**: Simple assignment (`=`) and compound assignment (`+=`, `-=`).
6. **Relational / Comparison Operators**: `==`, `!=`, `<`, `>`, `<=`, `>=`.
7. **Logical Operators**: `and`, `or`, `not` for multi-condition branching.
8. **Membership Operators**: `in` and `not in` for checking dictionary keys, character validity, and frozen sets.
9. **Identity Operators**: `is` and `is not` to verify against `None` when handling invalid divisions and summaries.
10. **Bitwise Operators**: `&` (bitwise AND) to check the least significant bit (LSB) for number parity (even/odd).
11. **`type()` Function**: Inspecting and displaying data types of inputs and calculation results.
12. **Type Conversion**: Converting string inputs to numbers using `int()` and `float()`.
13. **Division with Mixed Data Types**: Handling mixed integer and float calculations and displaying resulting types.
14. **Operator Precedence and Associativity**: Grouping expressions with parentheses for mathematical order of operations in summary statistics.
15. **Lists**: Dynamic collection `self.history` storing chronological calculation records.
16. **Tuples**: Immutable grouped records `(num1, symbol, num2, result)` and menu definition entries.
17. **Sets**: `self.unique_operators` tracking unique operator symbols executed in the session.
18. **Frozen Sets**: `ZERO_DIVISORS = frozenset({'/', '//', '%'})` for an immutable collection of operators requiring non-zero divisors.
19. **Dictionaries**: `OPERATIONS_MAP` mapping menu choices to operation names, symbols, and functions.
20. **Control Flow Statements**: `if`, `elif`, `else` conditional logic.
21. **Loops**: `while` loops for repeating the calculator menu and input validation; `for` loops for history iteration.
22. **Functions**: Modular functions for each mathematical operation and user interface task.
23. **Modules and Packages**: Project organized across `operations.py`, `calculator.py`, and `main.py`.
24. **Array Data Structure**: Built-in `array('d')` from the standard Python `array` module for numerical result storage.
25. **Object-Oriented Programming (OOP)**: A clean `Calculator` class with standard attributes and methods.

---

## 4. Project Structure

```text
Basic-Math-Calculator/
│
├── main.py                 # Main user interface, input validation, and execution loop
├── calculator.py           # Calculator class managing history, array storage, and summary
├── operations.py           # Pure math functions for arithmetic operations
├── tests/
│   └── test_project.py     # Simple test suite using plain Python assert statements
├── README.md               # Beginner-friendly documentation and guide
└── PROJECT_REPORT.md       # Academic project report
```

---

## 5. Requirements

* **Python 3.8 or higher**
* **External Dependencies**: None. The project strictly uses built-in Python standard library modules (`array`, `sys`, `os`).

---

## 6. Installation & Setup

1. Open your terminal / command prompt.
2. Navigate to the project directory:
   ```bash
   cd Basic-Math-Calculator
   ```
3. No package installation (`pip install`) is required.

---

## 7. How to Run

### Run the Main Calculator Program:
```bash
python main.py
```
*(On some systems, use `python3 main.py`)*

### Run the Automated Tests:
```bash
python tests/test_project.py
```

---

## 8. Example Usage

```text
================================
     BASIC MATH CALCULATOR      
================================
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Floor Division
6. Modulus
7. Power
8. Exit
================================
Enter your choice (1-8): 1

--- Selected Operation: Addition (+) ---
Enter the first number: 12
Enter the second number: 8

[Type Check] Operand 1: 12 (int), Operand 2: 8 (int)
Calculation Result: 12 + 8 = 20
[Type Check] Result type: int
[Bitwise Property] 20 is Even (verified via: int(result) & 1)
```

---

## 9. Sample Output

### Division by Zero Handling:
```text
Enter your choice (1-8): 4

--- Selected Operation: Division (/) ---
Enter the first number: 25
Enter the second number: 0

[Type Check] Operand 1: 25 (int), Operand 2: 0 (int)
Error: Division by zero is not allowed for Division (/)!
```

### Exit and Session Report:
```text
Enter your choice (1-8): 8

Exiting calculator...

--------------------------------
    SESSION HISTORY & REPORT    
--------------------------------
Calculation History:
  1. 12 + 8 = 20
  2. 17 // 3 = 5

Summary Statistics:
  Total calculations: 2
  Sum of all results: 25.0
  Average result:     12.50
  Unique operations:  2
  Operators used:     {'//', '+'}

Thank you for using Basic Math Calculator! Goodbye.
```

---

## 10. How Each Major Python Concept is Implemented

* **No Exception Handling**: All input validation is done via `is_valid_number()` using loop traversal, character checks (`>= '0'` and `<= '9'`), and decimal count tracking (`decimal_count <= 1`).
* **Identity Operators (`is`, `is not`)**: Used strictly where appropriate—comparing against `None` when division by zero occurs or when checking whether summary data exists.
* **Bitwise Operator (`&`)**: `int(number) & 1` inspects the least significant bit in binary to determine even/odd parity without using the modulus operator.
* **Array (`array('d')`)**: Stores floating-point results in a compact numerical array to compute the session average.
* **Frozen Set (`frozenset`)**: Defines `ZERO_DIVISORS = frozenset({'/', '//', '%'})` as an immutable set of operations requiring a non-zero divisor.
* **Tuples**: Each calculation entry is created as an immutable 4-tuple `(num1, op_symbol, num2, result)` so that past records cannot be accidentally modified.

---

## 11. Author

* **Course**: Python Essentials (First-Year University Coursework)
* **Project**: Basic Math Calculator
* **Year**: 2026

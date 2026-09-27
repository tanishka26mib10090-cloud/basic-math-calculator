# ACADEMIC PROJECT REPORT: BASIC MATH CALCULATOR

**Course**: Python Essentials (First-Year University Coursework)  
**Subject Code**: CS-101  
**Project Title**: Basic Math Calculator  
**Environment**: Standard Python 3 (Command-Line Interface)  

---

## 1. Title

**Basic Math Calculator in Python**

---

## 2. Introduction

The **Basic Math Calculator** is a console-based software application designed and implemented as part of the first-year university Python Essentials curriculum. The purpose of this project is to apply core procedural programming and introductory object-oriented programming concepts in Python to build an interactive, user-friendly calculator. The application executes basic arithmetic calculations, verifies inputs, prevents arithmetic runtime errors such as division by zero, and logs calculation records for the user session.

---

## 3. Problem Statement

Beginners using simple command-line programs often encounter input errors, program crashes due to unhandled zero divisions, or the lack of calculation tracking across multiple steps. Furthermore, educational projects often require demonstrating fundamental programming syllabus topics (such as variables, operators, loops, functions, basic data structures, and simple classes) without relying on high-level third-party libraries or advanced frameworks. 

The goal of this project is to develop a reliable, menu-driven calculator that:
1. Solves basic mathematical operations accurately.
2. Safeguards against invalid numeric inputs and division by zero using fundamental conditional logic.
3. Records calculation history and session statistics.
4. Naturally incorporates all 28 topics from the introductory Python syllabus.

---

## 4. Objectives

The primary objectives of this project are:
* To implement the seven fundamental arithmetic operations: addition, subtraction, multiplication, division, floor division, modulus, and exponentiation.
* To provide a clear text-based menu that allows users to perform multiple calculations in a single continuous session.
* To validate user inputs without using exception-handling blocks (`try/except`), adhering strictly to syllabus boundaries.
* To demonstrate the appropriate use of built-in Python data structures: lists, tuples, sets, frozen sets, dictionaries, and standard arrays.
* To introduce beginner-level object-oriented programming by organizing calculator state and history within a simple class.
* To write an automated test script using plain Python `assert` statements.

---

## 5. Technologies Used

* **Programming Language**: Python 3 (standard installation)
* **User Interface**: Terminal / Command-Line Interface (CLI)
* **Standard Library Modules**:
  * `array` (for numerical float array storage)
  * `sys` and `os` (for test script path configuration)
* **External Dependencies**: None (no third-party packages, no GUI frameworks, no databases)

---

## 6. Python Concepts Used

The project integrates the following syllabus concepts:

1. **Python Fundamentals**: Clear formatting, readable indentation, header comments, docstrings, and standard execution guard (`if __name__ == '__main__':`).
2. **Input and Output Operations**: Reading user input using `input()` and presenting clean formatted text using `print()`.
3. **Variables**: Storing numbers, strings, counters, and collection references.
4. **Arithmetic Operators**: `+` (addition), `-` (subtraction), `*` (multiplication), `/` (float division), `//` (floor division), `%` (modulus), and `**` (exponentiation).
5. **Assignment Operators**: Basic assignment (`=`) and in-place addition (`+=`) for counting operations and accumulating array sums.
6. **Relational / Comparison Operators**: `==`, `!=`, `<`, `>`, `<=`, and `>=` for range checking and zero-divisor detection.
7. **Logical Operators**: `and` (combining valid character checks), `or` (checking exit conditions), and `not` (re-prompting on invalid inputs).
8. **Membership Operators**: `in` (checking dictionary keys and frozen set elements) and `not in` (verifying characters).
9. **Identity Operators**: `is` and `is not` to test whether division by zero returned `None` and to confirm valid session summaries.
10. **Bitwise Operators**: Bitwise AND (`& 1`) to check the least significant bit (LSB) to determine if an integer result is even or odd.
11. **`type()` Function**: Displaying data types of user-entered numbers and computed results.
12. **Type Conversion**: Explicit conversion using `int()` and `float()`.
13. **Division with Mixed Data Types**: Handling division operations involving both integers and floats.
14. **Operator Precedence and Associativity**: Applying parentheses to specify execution order in average calculations: `(total_sum + 0.0) / count`.
15. **Lists**: Dynamic mutable list (`self.history`) storing the ordered history of calculations.
16. **Tuples**: Immutable 4-element tuples `(num1, op_symbol, num2, result)` representing permanent calculation records.
17. **Sets**: `self.unique_operators` tracking distinct operation symbols used.
18. **Frozen Sets**: `ZERO_DIVISORS = frozenset({'/', '//', '%'})` storing fixed operator symbols that cannot take zero as the second operand.
19. **Dictionaries**: `OPERATIONS_MAP` mapping menu choice keys (`'1'`, `'2'`, etc.) to tuples containing the operation name, operator symbol, and function pointer.
20. **Control Flow Statements**: `if`, `elif`, `else` multi-way branching.
21. **Loops**: `while` loops for the interactive menu cycle and input validation; `for` loop for iterating through history and results.
22. **Functions**: Modular functions in `operations.py` and `main.py`.
23. **Modules and Packages**: Separation of concerns into `operations.py`, `calculator.py`, and `main.py`.
24. **Array Data Structure**: Built-in `array('d')` from Python's standard `array` module for numerical result storage.
25. **Object-Oriented Programming**: A clean, beginner-level `Calculator` class with constructor `__init__`, standard attributes, and methods.

---

## 7. Project Design

### Module Breakdown
* **`operations.py`**: A pure mathematical module containing single-purpose functions for each of the seven arithmetic operations. It checks for zero divisors and returns `None` safely.
* **`calculator.py`**: Contains the `Calculator` class, which manages the application's state, history list, array of numerical results, and unique operator set.
* **`main.py`**: Contains the terminal user interface, loop management, numeric string parser, bitwise parity checker, and formatted report printer.
* **`tests/test_project.py`**: A dedicated test suite utilizing plain `assert` statements to ensure logic correctness across all operations.

---

## 8. Working of the Calculator

1. **Initialization**: When `main.py` is executed, an instance of `Calculator` is created.
2. **Menu Display**: The user is presented with a numbered menu displaying the seven operations and the Exit option.
3. **Input & Validation**:
   * The user selects an option from `1` to `8`.
   * If an operation (`1`–`7`) is chosen, the user is prompted to enter two operands.
   * `is_valid_number()` inspects the input string without `try/except`. If the input contains letters, extra decimal points, or invalid symbols, the user is prompted again.
   * Valid numbers are parsed into `int` or `float`.
4. **Zero-Division Check**: If the operation symbol belongs to `ZERO_DIVISORS` and the second operand is `0`, a descriptive error message is shown, preventing zero-division errors.
5. **Execution & History Logging**:
   * The selected operation function executes.
   * The calculation record is bundled as an immutable tuple `(num1, op_symbol, num2, result)` and stored in `calc.history`.
   * The result is appended to `calc.results_array`.
   * The operator symbol is added to `calc.unique_operators`.
6. **Bitwise Parity Inspection**: If the result is a whole number, its even/odd status is evaluated via `int(result) & 1` and displayed to the user.
7. **Session Summary on Exit**: When option `8` is selected, the application displays all past calculation records, the total count, the sum and average of results, and the set of unique operators used, before terminating cleanly.

---

## 9. Sample Inputs and Outputs

### Sample 1: Standard Addition
* **Input**: Option `1`, First number: `14`, Second number: `6`
* **Output**:
  ```text
  [Type Check] Operand 1: 14 (int), Operand 2: 6 (int)
  Calculation Result: 14 + 6 = 20
  [Type Check] Result type: int
  [Bitwise Property] 20 is Even (verified via: int(result) & 1)
  ```

### Sample 2: Zero Divisor Protection
* **Input**: Option `4` (Division), First number: `15`, Second number: `0`
* **Output**:
  ```text
  [Type Check] Operand 1: 15 (int), Operand 2: 0 (int)
  Error: Division by zero is not allowed for Division (/)!
  ```

### Sample 3: Floating-Point Power
* **Input**: Option `7` (Power), First number: `9`, Second number: `0.5`
* **Output**:
  ```text
  [Type Check] Operand 1: 9 (int), Operand 2: 0.5 (float)
  [Notice] Mixed data type operation detected: int and float
  Calculation Result: 9 ** 0.5 = 3.0
  [Type Check] Result type: float
  [Bitwise Property] 3 is Odd (verified via: int(result) & 1)
  ```

---

## 10. Testing

Testing was conducted using a dedicated script `tests/test_project.py` using standard Python `assert` statements. No external testing frameworks (like `unittest` or `pytest`) were used.

### Test Cases Covered:
1. **Addition**: Positive numbers, negative numbers, floating-point numbers.
2. **Subtraction**: Standard subtractions and negative-yielding differences.
3. **Multiplication**: Multiplications with positive, negative, and decimal values.
4. **Division**: Standard floating-point quotient; verifying `divide(x, 0) is None`.
5. **Floor Division**: Integer quotient; verifying `floor_divide(x, 0) is None`.
6. **Modulus**: Remainder calculation; verifying `modulus(x, 0) is None`.
7. **Power**: Integer powers and fractional powers (square roots).
8. **Input Validation**: Verified valid inputs (`"42"`, `"-15"`, `"3.14"`) and rejected invalid strings (`"abc"`, `"1.2.3"`, `"-"`, `""`).
9. **Bitwise Parity**: Confirmed accurate detection of even/odd integers (including zero and negative integers).
10. **State Tracking**: Confirmed that `Calculator` properly stores records in `history` (tuples), `results_array` (array), and `unique_operators` (set), and accurately computes session averages.

**Result**: All 12 test categories passed with 100% success rate.

---

## 11. Limitations

* The program runs only in a terminal environment; it does not feature a graphical user interface (GUI).
* Calculations are performed sequentially with two operands at a time, rather than parsing complex multi-variable algebraic expressions (e.g., `3 + 5 * (2 - 1)`).
* Calculation history is stored in memory during the active session and is not persisted to external disk files or databases.
* Very large floating-point exponents may reach Python's standard float representation limits.

---

## 12. Conclusion

The **Basic Math Calculator** successfully demonstrates how all foundational Python programming concepts can be harmoniously integrated into an effective, practical project. By structuring the code cleanly into distinct modules and avoiding complex external libraries or forbidden features, the project remains completely understandable for a first-year student while remaining robust and error-free.

---

## 13. Future Scope

While keeping the project accessible to first-year students, future iterations could include:
1. **File Persistence**: Saving calculation history to a text file using basic file I/O operations (`open()`, `write()`).
2. **Expression Evaluation**: Expanding the parser to evaluate chained operations in order of precedence.
3. **Scientific Functions**: Adding basic mathematical functions such as factorials, logarithms, and trigonometric calculations using Python's standard `math` module.

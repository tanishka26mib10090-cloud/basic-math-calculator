# main.py
# Basic Math Calculator - Main Program Module
# Handles user interaction, input validation (without try/except),
# menu display, operation execution, and session summary.

import operations
from calculator import Calculator, ZERO_DIVISORS

# Dictionary mapping menu choice strings to operation details:
# Key: Choice number string
# Value: Tuple containing (Operation Name, Symbol, Function Reference)
OPERATIONS_MAP = {
    '1': ('Addition', '+', operations.add),
    '2': ('Subtraction', '-', operations.subtract),
    '3': ('Multiplication', '*', operations.multiply),
    '4': ('Division', '/', operations.divide),
    '5': ('Floor Division', '//', operations.floor_divide),
    '6': ('Modulus', '%', operations.modulus),
    '7': ('Power', '**', operations.power)
}


def is_valid_number(text):
    """
    Validates whether an input string represents a valid integer or float.
    Implemented without try/except using basic string checks and loops.
    """
    cleaned = text.strip()

    if len(cleaned) == 0:
        return False

    # Check for optional leading sign
    start_index = 0
    if cleaned[0] == '-' or cleaned[0] == '+':
        if len(cleaned) == 1:
            return False  # A sign alone is not a valid number
        start_index = 1

    decimal_count = 0
    digit_count = 0

    index = start_index
    while index < len(cleaned):
        char = cleaned[index]
        if char == '.':
            decimal_count += 1
        elif char >= '0' and char <= '9':
            digit_count += 1
        else:
            # Found a character that is neither a digit nor a decimal point
            return False
        index += 1

    # A valid number must have at least one digit and at most one decimal point
    if digit_count > 0 and decimal_count <= 1:
        return True
    else:
        return False


def parse_number(text):
    """
    Converts a validated numeric string into an int or float.
    Demonstrates type conversion.
    """
    cleaned = text.strip()
    # Membership operator 'in' to check if a decimal point exists
    if '.' in cleaned:
        return float(cleaned)
    else:
        return int(cleaned)


def get_number_input(prompt_text):
    """
    Prompts the user until a valid number is entered.
    Uses while loop, logical not, and input/output operations.
    """
    valid = False
    number_value = 0
    while not valid:
        user_input = input(prompt_text)
        # Logical NOT operator to check validation condition
        if not is_valid_number(user_input):
            print("Error: Invalid numeric input! Please enter a valid number (e.g., 10 or 3.5).")
        else:
            number_value = parse_number(user_input)
            valid = True
    return number_value


def check_parity_bitwise(number):
    """
    Determines if an integer number is Even or Odd using the bitwise AND operator (&).
    In binary representation, the least significant bit (LSB) is 0 for even numbers
    and 1 for odd numbers.
    """
    integer_value = int(number)
    if integer_value & 1 == 0:
        return "Even"
    else:
        return "Odd"


def display_menu():
    """
    Displays the user interface menu for the calculator.
    """
    print("\n================================")
    print("     BASIC MATH CALCULATOR      ")
    print("================================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Modulus")
    print("7. Power")
    print("8. Exit")
    print("================================")


def show_session_summary(calc):
    """
    Displays the calculation history and session summary.
    Demonstrates List, Tuple, Set, and Array traversal.
    """
    history_list = calc.get_history()

    print("\n--------------------------------")
    print("    SESSION HISTORY & REPORT    ")
    print("--------------------------------")

    if len(history_list) == 0:
        print("No calculations were performed in this session.")
        return

    print("Calculation History:")
    record_number = 1
    # Iterate through history list containing calculation tuples
    for item in history_list:
        num1, symbol, num2, result = item
        print(f"  {record_number}. {num1} {symbol} {num2} = {result}")
        record_number += 1

    # Retrieve summary tuple from Calculator instance
    summary = calc.get_summary()

    # Identity operator 'is not' to check that summary was calculated
    if summary is not None:
        total_ops, total_sum, avg_result, unique_ops_count = summary
        print("\nSummary Statistics:")
        print(f"  Total calculations: {total_ops}")
        print(f"  Sum of all results: {total_sum}")
        print(f"  Average result:     {avg_result:.2f}")
        print(f"  Unique operations:  {unique_ops_count}")
        print(f"  Operators used:     {calc.unique_operators}")


def main():
    """
    Main function executing the calculator lifecycle.
    """
    # Create an instance of the Calculator class
    calc = Calculator()

    running = True

    while running:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()

        # Logical OR to handle exit selection
        if choice == '8' or choice.lower() == 'exit':
            print("\nExiting calculator...")
            show_session_summary(calc)
            print("\nThank you for using Basic Math Calculator! Goodbye.")
            running = False

        # Membership operator 'in' to check if choice exists in dictionary
        elif choice in OPERATIONS_MAP:
            op_name, op_symbol, op_func = OPERATIONS_MAP[choice]
            print(f"\n--- Selected Operation: {op_name} ({op_symbol}) ---")

            num1 = get_number_input("Enter the first number: ")
            num2 = get_number_input("Enter the second number: ")

            # Demonstrate type() function on inputs
            print(f"\n[Type Check] Operand 1: {num1} ({type(num1).__name__}), Operand 2: {num2} ({type(num2).__name__})")

            # Check for mixed data types in calculation
            if type(num1) != type(num2):
                print(f"[Notice] Mixed data type operation detected: {type(num1).__name__} and {type(num2).__name__}")

            # Safe division check: verify if operator requires non-zero divisor
            # Uses membership operator 'in' with frozen set ZERO_DIVISORS
            # and comparison operator '=='
            if op_symbol in ZERO_DIVISORS and num2 == 0:
                print(f"Error: Division by zero is not allowed for {op_name} ({op_symbol})!")
            else:
                # Perform the calculation
                result = op_func(num1, num2)

                # Check result using identity operator 'is'
                if result is None:
                    print(f"Error: Calculation could not be performed (invalid divisor).")
                else:
                    # Identity operator 'is not' to ensure valid calculation result
                    if result is not None:
                        calc.add_calculation(num1, op_symbol, num2, result)
                        print(f"Calculation Result: {num1} {op_symbol} {num2} = {result}")
                        print(f"[Type Check] Result type: {type(result).__name__}")

                        # Check if result is an integer or whole number to demonstrate bitwise parity
                        if result == int(result):
                            parity = check_parity_bitwise(result)
                            print(f"[Bitwise Property] {int(result)} is {parity} (verified via: int(result) & 1)")

        else:
            print("Invalid choice! Please select an option between 1 and 8.")


if __name__ == '__main__':
    main()

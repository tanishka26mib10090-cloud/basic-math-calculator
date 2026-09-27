# calculator.py
# Basic Math Calculator - Calculator Class Module
# Defines the Calculator class managing state, history, and numerical results.
# Demonstrates List, Tuple, Set, Frozen set, and the standard Array module.

from array import array

# A frozen set defining operators that cannot accept zero as the second operand (divisor)
# Demonstrates frozenset() for an immutable set of operator symbols
ZERO_DIVISORS = frozenset({'/', '//', '%'})


class Calculator:
    """
    A simple beginner-level Calculator class to store calculation records,
    track unique operations, and calculate summary statistics.
    """

    def __init__(self):
        # List data structure to store calculation history records
        self.history = []

        # Standard Python array of type 'd' (double precision float) for numerical results
        self.results_array = array('d')

        # Counter variable for total completed calculations
        self.operations_count = 0

        # Set data structure to store unique operator symbols used in this session
        self.unique_operators = set()

    def add_calculation(self, num1, op_symbol, num2, result):
        """
        Stores a completed calculation.
        Uses a tuple for the immutable calculation record: (num1, op_symbol, num2, result).
        Appends the numeric result to the results array.
        Increments the operation count using the assignment operator (+=).
        Adds the operator symbol to the unique operators set.
        """
        # Store as an immutable tuple
        record = (num1, op_symbol, num2, result)
        self.history.append(record)

        # Store numerical result in array (converts to float for array type 'd')
        self.results_array.append(float(result))

        # Update counter using assignment operator
        self.operations_count += 1

        # Add operator symbol to set
        self.unique_operators.add(op_symbol)

    def get_history(self):
        """
        Returns the list of calculation records.
        """
        return self.history

    def get_summary(self):
        """
        Calculates and returns a summary tuple of the session.
        Demonstrates loops, array traversal, and operator precedence.
        Returns None if no operations have been performed.
        """
        if self.operations_count == 0:
            return None

        # Calculate sum of all numeric results stored in the array
        total_sum = 0.0
        for val in self.results_array:
            total_sum += val

        # Operator precedence: grouping expression with parentheses
        average_result = (total_sum + 0.0) / self.operations_count

        # Return a fixed summary tuple: (count, total_sum, average_result, unique_ops_count)
        return (self.operations_count, total_sum, average_result, len(self.unique_operators))

    def clear_history(self):
        """
        Clears all stored history records and resets counters.
        """
        self.history = []
        self.results_array = array('d')
        self.operations_count = 0
        self.unique_operators = set()

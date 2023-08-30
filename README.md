# Algebraic Expression Evaluator

This Python program allows you to evaluate and simplify algebraic expressions, including those involving variables. The program uses the SymPy library for parsing, evaluation, and simplification of algebraic expressions.

## Features

- Evaluate basic arithmetic expressions (e.g., addition, subtraction, multiplication, division).
- Calculate exponentiation using the `^` operator for both numbers and variables (a, b, c, d).
- Simplify expressions containing variables (a, b, c, d) to their simplest form.
- Detect and handle invalid expressions or operations, as outlined in the task description.

## Usage

1. Clone this repository to your local machine.
2. Install the required libraries by running `pip install sympy`.
3. Run the script `algebraic_expression_evaluator.py`.
4. Enter an algebraic expression when prompted. Follow the rules provided in the task description.

## Example
Enter an algebraic expression: (a + 42) * (a + 42) + (a + 42)
Expression: (a + 42) * (a + 42) + (a + 42)
Result: a^2 + 85a + 1806


## Rules

- The program follows the specified rules for valid and invalid expressions, as described in the task.
- Exponentiation is calculated using the `^` operator for both numbers and variables.
- Expressions with variables will be simplified to their simplest form.

## Contributions

Contributions are welcome! If you find any issues or want to add enhancements, feel free to create pull requests.


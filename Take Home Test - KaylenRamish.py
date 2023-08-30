"""
This programe calculates and simplifies all equations including variables and
simplifies the result

"""
from sympy import *

# Function to simplify an algebraic expression
def simplify_algebraic_expression(expression_str):
    x, a, b, c, d = symbols('x a b c d')
    try:
        expression = parse_expr(expression_str)
        expanded_expression = expand(expression)  # Expand the expression first
        simplified_expression = simplify(expanded_expression)
        return str(simplified_expression)
    except (SyntaxError, TypeError, ValueError):
        return "Invalid Expression"

# Function to evaluate an algebraic expression
def evaluate_algebraic_expression(expression_str):
    """
    Evaluates an algebraic expression.

    Args:
        expression_str (str): The input algebraic expression.

    Returns:
        str: Evaluated algebraic expression or "Invalid Expression" if unable to evaluate.
    """
    x, a, b, c, d = symbols('x a b c d')
    try:
        expression = parse_expr(expression_str)
        simplified_expression = simplify(expression)
        return str(simplified_expression)
    except (SyntaxError, TypeError, ValueError):
        return "Invalid Expression"

# Function to check if an expression contains specified variables
def contains_variables(expression_str, variables):
    for var in variables:
        if var in expression_str:
            return True
    return False

#Function to check if an expression has a double operator as shown in task resource this will output invalid
def has_double_operator(expression_str):

    """This rule does not impact integers, as these calculations require a space between 
    integer value and operator eg. 1 + -3 """

    double_operators = ['++', '--', '**', '//', '^^', '+-', '-+', '*-', '/-']
    for operator in double_operators:
        if operator in expression_str:
            return True
    return False

# Function to check for number or variable next to bracket with no operator
def has_number_or_variable_next_to_bracket(expression_str):
    variables = ['a', 'b', 'c', 'd']
    for i in range(len(expression_str) - 1):
        if (expression_str[i].isdigit() or expression_str[i] in variables) and expression_str[i + 1] == '(':
            return True
    return False

# Function to replace ** with ^ for results involving variables, Not applied to real numbers 
def replace_exponentiation_with_operator(expression_str):
    variables = ['a', 'b', 'c', 'd']
    for var in variables:
        if var in expression_str:
            expression_str = expression_str.replace('**', '^')
    return expression_str.replace('*', '')  # Remove * character when followed by a variable

# Get user input for an algebraic expression
user_input = input("Enter an algebraic expression: ")

# Process user input and generate output
# Handle desired outputs as outlined 
if has_double_operator(user_input) or has_number_or_variable_next_to_bracket(user_input):
    result = "Invalid Expression"
else:
    try:
        if "^" in user_input:
            base, exponent = user_input.split("^")
            base_expr = parse_expr(base)
            exponent_expr = parse_expr(exponent)
            if base in ["a", "b", "c", "d"]:
                result = f"{base} ^ {exponent}"  # Display result with ^ operator for variables
            else:
                result = str(base_expr ** exponent_expr)  # Calculate exponentiation for numbers
                result = result.replace("**", "^")  # Replaces ** with ^ for numbers
        else:
            result = evaluate_algebraic_expression(user_input)
            if contains_variables(result, ["a", "b", "c", "d"]):
                result = simplify_algebraic_expression(result)  # Simplify result with variables
                result = replace_exponentiation_with_operator(result)  # Replace ** with ^ for variables
    except:
        result = "Invalid Expression"

print(f"Expression: {user_input}")
print(f"Result: {result}")

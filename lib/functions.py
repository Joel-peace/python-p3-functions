# When we define a function with no parameters, we still need the parentheses
# Note: In Python, we use snake_case for function names instead of camelCase
def greet_programmer():
    # print() automatically adds a newline unless we tell it otherwise
    print("Hello, programmer!")
    # Python functions return None by default if there's no return statement

# This function REQUIRES one argument when called (unlike JavaScript)
# Try calling greet() without arguments to see Python's helpful error message
def greet(name):
    # f-strings are like JS template literals but with f before the quotes
    # Python will replace {name} with the value of the name parameter
    print(f"Hello, {name}!")

# The = "programmer" sets a default value for the name parameter
# This makes it optional - we can call with or without arguments!
def greet_with_default(name="programmer"):
    # Default parameters must come after required parameters in the list
    # (Not an issue here since we only have one parameter)
    print(f"Hello, {name}!")

# Python is particular about spacing around operators in function definitions
# Notice the spaces around the + operator in the return statement
def add(num1, num2):
    # Python will automatically return integers or floats based on input
    # Try calling add(2, 3) vs add(2.5, 3.5) to see the difference
    return num1 + num2

# Division in Python behaves differently than JavaScript:
# - Single / does floating point division (returns float)
# - Double // does integer division (truncates decimal)
def halve(number):
    # Even if input is an integer (like 4), this returns a float (2.0)
    # To get integer output, we'd need to use // or convert to int
    return number / 2
    # Fun fact: Try halve(5) to get 2.5 vs what JS would give you!
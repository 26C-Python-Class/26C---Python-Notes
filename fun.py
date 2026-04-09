def function_name(parameters):
    # This is the "body" of the function
    result = parameters * 2
    return result

# Simple function
def say_hi():
    print("Hello there!")

say_hi()  # Calling the function

# Functions with multiple arguments
def add_numbers(a, b):
    return a + b

sum_total = add_numbers(5, 10)
print(sum_total) # Output: 15

# Functions with default parameters/arguments
def greet(name="Guest"):
    print(f"Welcome, {name}!")

greet("Alice") # Output: Welcome, Alice!
greet()        # Output: Welcome, Guest!
# Use docstrings to explain what your function does
def square(n):
    """Returns the square of a number."""
    return n * n
print(square(5))

# n Python, *args and **kwargs allow a function to accept a variable number of arguments. 
# This is useful when you don't know ahead of time how many inputs a user will provide.
# 1. *args (Non-Keyword Arguments)
# The * unpacks an sequence into a tuple. Use this when you want to pass a list of items 
# without predefined names.
def add_all(*nums):
    # 'nums' is treated as a tuple (1, 2, 3)
    return sum(nums)

print(add_all(1, 2, 3, 4, 5)) # Output: 15

# 2. **kwargs (Keyword Arguments)
# The ** unpacks data into a dictionary. Use this when your inputs have labels (keys).
def print_profile(**info):
    # 'info' is treated as a dictionary {'name': 'Alice', 'age': 25}
    for key, value in info.items():
        print(f"{key}: {value}")

print_profile(name="Alice", age=25, job="Dev")



# Fruitful and void functions

#The return statement exits a function and sends a 
# specific value back to the line of code that called it. 
# Think of it as the function "handing over" its final result.
def add(a, b):
    return a + b

result = add(5, 3)  # 'result' now holds the value 8

def check_age(age):
    if age < 18:
        return "Access Denied"
    return "Welcome!"  # This only runs if age >= 18
def get_user():
    name = "Alice"
    age = 30
    return name, age  # Returns both

user_name, user_age = get_user()

def no_return():
    print("I did something!")

val = no_return()
print(val)  # Output: None
#Pro Tip: Use return when you need to use the calculation later; 
# use print() only when you just want to see the result on the screen.
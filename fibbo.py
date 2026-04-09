# Fibonacci using recursion

def fibonacci_recursive(n):
    # If statements define the base cases (0 and 1)
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive step
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Printing the first 10 terms
for i in range(10):
    print(fibonacci_recursive(i), end=" ")

# Using if conditions loop
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

for i in range(1, 101):
    output = ""
    if i % 3 == 0: output += "Fizz"
    if i % 5 == 0: output += "Buzz"
    
    # If output is still empty, just print the number
    print(output or i)

# Using a lambda function    
fizzbuzz = lambda i: "FizzBuzz" if i % 15 == 0 else ("Fizz" if i % 3 == 0 else ("Buzz" if i % 5 == 0 else i))

for i in range(1, 101):
    print(fizzbuzz(i))



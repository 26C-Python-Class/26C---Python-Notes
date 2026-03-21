"""
Starter Lab: 02_operators
"""

result = (10 + 5) * 2
print(f'Logic Check: {result > 20 and True}')

### 1. Parentheses `()`
# Parentheses always take top priority. They are used to override any other operator.

# Without parentheses: 2 + 3 * 4 = 14
# With parentheses:
result = (2 + 3) * 4 
print(result)  # Output: 20


### 2. Exponentiation `**`
# Calculates power before any basic math.

# 2 * 3 squared (3**2 = 9)
result = 2 * 3 ** 2 
print(result)  # Output: 18


### 3. Unary Operators `+x`, `-x`, `~x`
# These act on a single number (positive, negative, or bitwise NOT).

x = 10
print(-x)      # Output: -10
print(~5)      # Bitwise NOT (Inverts bits): Output: -6


### 4. Multiplication, Division, Floor, Modulus `*`, `/`, `//`, `%`
# These are handled left-to-right before addition.

print(10 / 2 * 3)   # 5.0 * 3 = 15.0
print(10 // 3)      # Floor division: 3
print(10 % 3)       # Modulus (remainder): 1


### 5. Addition and Subtraction `+`, `-`

print(10 - 5 + 2)   # 5 + 2 = 7


### 6. Bitwise Shifts `<<`, `>>`

print(2 << 2)  # Binary 10 becomes 1000: Output: 8
print(8 >> 1)  # Binary 1000 becomes 100: Output: 4


### 7. Bitwise AND `&`

# Binary: 5 (101) & 3 (011) = 1 (001)
print(5 & 3)   # Output: 1


### 8. Bitwise XOR `^` and OR `|`

print(5 ^ 3)   # XOR: Output: 6
print(5 | 3)   # OR:  Output: 7


### 9. Comparisons, Identity, and Membership
# Includes `==`, `!=`, `>`, `<`, `is`, and `in`. These are all at the same level.

list_a = [1, 2, 3]
print(2 in list_a)          # Membership: True
print(5 > 3 == True)        # Comparison: False (because 3 == True is False)
print(list_a is not None)   # Identity: True

### 10. Logical `not`

print(not True == False)    # "not True" is False, False == False is True.


### 11. Logical `and`
# 'and' is evaluated before 'or'
print(True or False and False) # True or (False) = True

### 12. Logical `or`
print(False or True) # Output: True

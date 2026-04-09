# A lambda function also termed as an anonymous function has no name
# Contains only one expression
# auto returns no typing return
# keyword parameter : expression

add_ten = lambda x: x + 10
print(add_ten(5))  # Output: 15

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
# Result: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
# Result: [2, 4, 6]

#lambda arguments: value_if_true if condition else value_if_false

check_num = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check_num(10)) # Output: Even
print(check_num(7))  # Output: Odd

temps = [15, 22, 10, 30, 18]

# If temp > 20, it's 'Warm', otherwise it's 'Cold'
categories = list(map(lambda t: "Warm" if t > 20 else "Cold", temps))

print(categories) 
# Output: ['Cold', 'Warm', 'Cold', 'Warm', 'Cold']

# Label as Positive, Negative, or Zero
sign = lambda x: "Pos" if x > 0 else ("Neg" if x < 0 else "Zero")

print(sign(-5)) # Output: Neg

# Lambda inside other functions
users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 25}
]

# Sort the list by 'age'
users.sort(key=lambda user: user["age"])

print(users) 
# Output: [{'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 25}, ...]

nums = [1, 2, 3, 4, 5, 6]

# Map: Square every number
squared = list(map(lambda x: x**2, nums)) # [1, 4, 9, 16, 25, 36]

# Filter: Keep only numbers greater than 3
big_nums = list(filter(lambda x: x > 3, nums)) # [4, 5, 6]



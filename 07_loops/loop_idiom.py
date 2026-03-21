# In Python, loop idioms are common patterns or 
# "best practice" ways to perform standard tasks 
# within a loop. Instead of just writing a basic for 
# or while loop, idioms use specific logic to handle 
# data efficiently and readably.

# Think of them as the "phrases" of the programming 
# language—standard ways to solve recurring problems 
# like finding the largest number, counting items, or 
# filtering a list.
numbers = [3, 41, 12, 9, 74, 15]
largest = None 

for num in numbers:
    if largest is None or num > largest:
        largest = num
    print(f"Current: {num}, Largest so far: {largest}")

print(f"Final Largest: {largest}")


smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Smallest:', smallest)

numbers = [10, 20, 30, 40]
total = 0  # Initialize

for num in numbers:
    total = total + num  # Accumulate

print(f"Total: {total}")

# The counter idiom
words = ["apple", "banana", "apple", "cherry", "apple"]
count = 0

for word in words:
    if word == "apple":
        count += 1

print(f"Apple appeared {count} times.")

# Search idiom(check existence)
found = False
search_for = 3
data = [9, 41, 12, 3, 74, 15]

for value in data:
    if value == search_for:
        found = True
        break  # Efficiency: stop looking once found

print(f"Found {search_for}? {found}")

# Filtering idiom
original_data = [1, 5, 10, 15, 20]
filtered_data = []

for val in original_data:
    if val > 10:
        filtered_data.append(val)

print(f"Numbers greater than 10: {filtered_data}")
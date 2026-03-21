"""
Starter Lab: 07_loops. For loop also called definite loop.
Runs a specified number of times based on the set of items
"""

# for i in range(5):
#     print(f'Iteration {i}')
    
buddies = ["John", "Mary", "Njoki", "Tina", "Sam", "Favour"]
for friend in buddies:
    print(f"How are you doing: ", friend )
    
# Iteration over a string
mystring = "Python"        
for char in mystring:
    print(char)
    
# Iterating over a range of numbers
for i in range(1, 10):
    print("Counting :", i) 
    
#  The smart loop 
marks = [78, 89, 96, 99, 65,56]
print("Scanning marks...")
for mark in marks:
    if mark >= 90:
        print("Found the best student's score: ", mark)
        
# the break and continue
# We can use the break statement with the for loop to 
# terminate the loop when a certain condition is met. 
# For example,
for i in range(5):
    if i == 3:
        break
    print(i)  
    
# We can use the continue statement with the for loop to 
# skip the current iteration of the loop and jump to the next 
# iteration. For example,
for i in range(5):
    if i == 3:
        continue
    print(i)

          
#Conditionals
# If condition
language = "Python"
if language == "Python":
    print("Welcome to Python Programming!")

# Chained conditionals(if-elif-else)
age = 5
if age > 18:
    
    print("You are eligible to vote")
elif age < 18 and age > 12:# Short-circuit evaluation
    print("You are a minor")
else:
    print("You are a toddler")
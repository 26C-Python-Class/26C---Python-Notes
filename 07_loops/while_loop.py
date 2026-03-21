"""
    Runs until a condition is met
"""

x = 10
while x > 0: # Evaluation of the condition, if false exit
    print(x)
    x = x - 1 # Iteration step (variable changes on each iteration loop)
print("End of the loop")

# Print numbers until the user enters 0
number = int(input('Enter a number: '))

# iterate until the user enters 0
while number != 0:
    print(f'You entered {number}.')
    number = int(input('Enter a number: '))

print('The end.')

# The break and continue
secret = 7
while True:
    guess = int(input("Guess the number: "))
    if guess < 0:
        print("Positive numbers only!")
        continue
    if guess == secret:
        print("You win!")
        break
    print("Try again...")

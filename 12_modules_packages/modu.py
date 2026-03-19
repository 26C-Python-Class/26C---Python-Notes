import math

# Use the constant Pi
print(math.pi)  # Output: 3.141592653589793

# Calculate the area of a circle (Area = pi * r^2)
radius = 5
area = math.pi * (radius ** 2)
print("The area is:", area)

import math

print(math.sqrt(64))  # Output: 8.0 (Square root)
print(math.pow(2, 3)) # Output: 8.0 (2 to the power of 3)

import math

rating = 4.1

print(math.ceil(rating))  # Output: 5
print(math.floor(rating)) # Output: 4

import random

# Simulating a percentage (0.0 to 1.0)
chance = random.random()
print("Success rate:", chance)

# Simulating a 6-sided die roll
roll = random.randint(1, 6)
print("You rolled a:", roll)

import random

weather_options = ["Sunny", "Rainy", "Snowy", "Cloudy"]
today_weather = random.choice(weather_options)

print("Today's weather will be:", today_weather)

import random
import string

def generate_password(length=12):
    # characters = "abcdef...0123...!"
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly pick characters and join them into a string
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print(f"Random Password: {generate_password(16)}")

import secrets
import string

alphabet = string.ascii_letters + string.digits + string.punctuation
# secrets.choice is more secure than random.choice
secure_password = ''.join(secrets.choice(alphabet) for i in range(20))

print(f"Secure Password: {secure_password}")


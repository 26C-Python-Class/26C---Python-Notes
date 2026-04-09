import math
import random
import datetime
print(math.pi)

radius = 5
area = math.pi * (radius ** 2)
print(f"The area is:", area)

print(math.sqrt(64))

roll = random.randint(1, 6)
print("You rolled a: ", roll)

now = datetime.datetime.now()
print("The time now is: ", now)
print("Formatted time: ", now.strftime("%A, %B %d"))
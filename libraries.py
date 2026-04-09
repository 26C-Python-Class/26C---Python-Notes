import datetime
now = datetime.datetime.now()
print("The time is: ", now)
print("Current year: ", now.year)
print("Formatted time: ", now.strftime("%A, %B %d"))

import os

# Find out which folder your script is currently running in
where_am_i = os.getcwd()
print("I am running in:", where_am_i)

# List all files in the current folder
files = os.listdir()
print("Files in this folder:", files)

import statistics

scores = [85, 93, 45, 87, 93, 72, 81]

print("Average Score:", statistics.mean(scores))
print("Most Common Score:", statistics.mode(scores))
print("Middle Value:", statistics.median(scores))
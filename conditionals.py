# if the language is python then give a welcome message
language = "JavaScript"
if language == "Python":
    print("Welcome to python programming!")
else:
    print("Select your language!") 
    
# Short circuit evaluation
age = 11
if age > 18:
    print("You are an adult! Welcome to the club!")
elif age < 18 and age > 12:
    print("You are a teenager! You can go to class and read!")
else:
    print("You are a toddler!")          
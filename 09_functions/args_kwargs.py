# The *args syntax captures any additional positional arguments passed to a 
# function and stores them as a tuple. 
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3))        # Output: 6
print(sum_numbers(10, 20, 30, 40)) # Output: 100

# The **kwargs syntax captures additional named arguments (key=value pairs) 
# and stores them as a dictionary. 

def show_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_profile(name="Alice", age=25, city="Nairobi")
# Output:
# name: Alice
# age: 25
# city: Nairobi

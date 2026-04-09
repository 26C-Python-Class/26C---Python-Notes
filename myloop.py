buddies = ["John", "Mary", "Njoki", "Tina", "Sam", "Favour"]
for buddy in buddies:
    print(f"How are you {buddy}?")
    
for i in range(1, 10):
    print(i)   
    
# while loop
x = 10
while x > 0:
    print(x)
    x = x - 1 
print('End of the loop') 

# recursive function
nested = [1, [2, [3, 4], 5], 6, [7, 8]] 
def flatten(nested):
    flat_list = []
    for num in nested:
        if isinstance(num, list):
            flat_list.extend(flatten(num)) 
        else:
            flat_list.append(num) 
    return flat_list
print(flatten(nested))             
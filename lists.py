veges = []
print(type(veges))

data = [23, 45, ["french-fries", 'hamburger'], {'name:''Jane'}, True, False ]
# data[1] = "Grace"
# print(data)

print(45 in data)

for x in data:# List comprehension
    print(x)
    
numbers = [2, 3, 4, 5, 6, 7, 8]  

for number in range(len(numbers)):# n - 1
    numbers[number] = numbers[number] **3 
    
    print(numbers)
    
    
# A nested for loop is a programming construct where 
# one for loop is placed inside the body of another 
# for loop. This allows for iteration over multi-dimensional
# data structures or the execution of repetitive tasks
# that require multiple layers of iteration.

# Example printing a multiplication table 
for i in range(2, 4):
    for j in range(1, 11):
        print(i, "*", j, "=", i*j)
    print() 
    
# Printing statements
l1 = ['I am ', 'You are ']
l2 = ['healthy!', 'fine!', 'Zindua!']

l2_size = len(l2)
for item in l1:
  
    print("start outer for loop ")
    i = 0
    while(i < l2_size):
      
        print(item, l2[i])
        i = i+1
    print("end for loop ")    
# Break and continue
for i in range(2, 4):
    for j in range(1, 11):
      if i==j:
        break
      print(i, "*", j, "=", i*j)
    print()

for i in range(2, 4):
    for j in range(1, 11):
      if i==j:
        continue
      print(i, "*", j, "=", i*j)
    print()    
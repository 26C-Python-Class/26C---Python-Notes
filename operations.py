# PEDMAS

a = [2, 4, 6]
print(a * 2)
b = [3, 5, 7]
c = a + b
print(c)
print([2, 4, 6] *2)

my_list = ['Esther', 'Nancy', 'Belvah', 'Grace']
names = ['Mutheu', 'Wanjiru']
print(my_list[:])
my_list.append('Cynthia')
print(my_list)
my_list.extend(names)
print(my_list)
my_list.sort()
my_list.reverse()
print(my_list)
rm_name = my_list.pop()
print(rm_name)
named = my_list.remove('Nancy')
print(my_list)

del my_list[1:3]
print(my_list)

numbers = [23, 13, 42, 89, 5, 67, 17] 
print(len(numbers))
print(max(numbers))
print(sum(numbers))

# my_num = []
# while True:
#     num = input("Enter a number \n")
#     if num == 'done': break
#     all_nums = float(num)
#     my_num.append(all_nums)
    
# average = sum(my_num) / len(my_num)  
# print(f'The average is: {average}') 

name = "Mutheu"
my_list = list(name)
print(my_list)

name = 'Esther'
my_name = "Esther"
print(my_name is name)
# Implicit type conversion
integer_num = 25
float_num = 12.75
new_num = integer_num + float_num
print("Value:",  new_num)
print(type(new_num))# implicitly converts integer_num to float

# Explicit type conversion (type casting)
## We use built in functions like int(), float(), str() to perform explicit type conversion
num_str = '45'
num_int = 56

print('Data type of num_str before type casting: ', type(num_str))
# explicit type conversion
num_str  = int(num_str)

print('Data type of num_str after type casting: ', type(num_str))

sum = num_str + num_int
print("Sum: ", sum)
print("Data type of sum: ", type(sum))

num = "15.75"# Can not be directly converted to int() You get error of base 10
num = float(num)
print(num)



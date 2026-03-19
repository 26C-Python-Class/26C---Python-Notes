# Implicit type conversion
int_num = 25 # 
float_num = 12.75
sum = int_num + float_num
print("Value: ", sum)

# Explicit type conversion - type casting
num = "25"
print(type(num))
num1 = 120
num = int(num)
print(type(num))
sum = num + num1
print(sum)

num = 45
num2 = "12.75"
num2 = float(num2)
print(type(num2))
num2 = int(num2)
print(type(num2))
sum = num + num2
print(sum)
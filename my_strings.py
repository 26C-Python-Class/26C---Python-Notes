word = 'banana'
number = '45'
print(type(number))
print(word[4])
print(word[2])
# print(word[12])
print(len(word))

last_index = len(word) - 1
print(last_index)
print(word[last_index])

# Slicing - creates a substring
# [starting: stoppoint]

message = "Welcome to Python Programming"
print(len(message))
print(message[0:10])
print(message[:10])# start from zero
print(message[5:])# start from the defined index to the end
print(message[:])# Creates a copy of the string

number = '0725439354'
print(number[0::3])
print(number[::-1])
# message[1] = 'i'
language = 'Pithon'
corrected = language[0] + 'y' + language[2:]
print(corrected)


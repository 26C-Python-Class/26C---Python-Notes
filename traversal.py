word = 'banana'
index = 0

# while index < len(word):
#     x = word[index]
#     print(f'Index {index} contains: {x}')
#     index += 1

for char in word:
    if char == 'n':
        index = index + 1  
    print(index)      
# for char in word:
#     print(char) 
print('en' in word)   # returns a boolean
email = 'kwanusujoseph@gmail.com'
print('@gmail' in email)

fruit = 'Pineapple'
if word < 'Pineapple':
    print('banana comes first')
    
fruit.capitalize()    
# def sum_numbers(*args):
#     return sum(args)
# print(sum_numbers(12, 34))

# def show_profile(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# show_profile(name="Belvah", age=26, city="Nairobi")        


# While loop
# initialization step
# num = 1000
# while num > 0:
#     if num == 800:
#         break
#     print(num)
#     # increment step
#     num = num - 1
# print('Finished looping!')  

# word = 'Python'

# while True:
#     guess = str(input("Which is the most popular programming language in 2026?....\n"))
#     if guess == '':
#         print('Please enter a valid guess')
#         continue
#     if guess == word:
#         print('Congratulations, you guessed right!')
#         break
#     print('Nice attempt please try again another time')

my_num = 7  
while True:
    guess = int(input('Give me a prime number between 1 and 10 \n'))# 1
    if guess < 0:
        print("Enter a positive number") 
        continue
    if guess == my_num:
        print('Congratulations you made it!')  
        break
    print('Please try again...')    
            
          
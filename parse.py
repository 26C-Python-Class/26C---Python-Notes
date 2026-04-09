# Parsing data is analyzing a string to extract meaningful data

data = 'From stephen.marqued@co.ke Sat Feb 23 20:32:45 2021'
start_at = data.find('@')
print(start_at)
space = data.find(' ', start_at)
host = data[start_at + 1: space]
print(host)

name = "Joseph"
print(f"Welcome {name}")
doll = 'Disney' 
price = 5889.8765
print(f"The price of {doll} is ${price:,.2f}")

import os

if os.path.exists('mbox.txt'):
    print("The file has been found")
    print(f'The file is: {os.path.getsize('mbox.txt')} bytes')
else:
    print("The file not found")
    print(f'Current directory is: {os.getcwd()} ')  
    
# mode - w, r, a
# fhand = open('mbox.txt', 'w')
# data = fhand.read()
# print(data) 
# fhand.close()    
with open('mbox.txt', 'r') as file:
    with open('emails.txt', 'w', encoding='utf-8') as output:
        for line in file:
            if line.startswith('From:'):
                email = line.split()[1]
                output.write(email + '\n')   

# with open('mbox.txt', 'r', encoding='utf-8') as file:
#     # data = file.read()
#     for line in file:
#         line = line.rstrip()
#         if len(line) == 0: continue
#         if line.startswith('From:'):
#             continue
#         if '@utc.ac.za' not in line:
#             continue
#         # if '2008' in line:
#     print(line)
    
# import sys

# fname = input("Enter the file name...\n")

# try:
#     with open(fname, 'r', encoding='utf-8') as file:
#         count = 0
#         for line in file:
#             count += 1
#         print(f"Got {count} lines")  
# except FileNotFoundError:
#     print(f"Error: The file {fname} does not exist. Please check the spelling and try again.")              
# except PermissionError:
#     print(f"Error: You do not have permission to open {fname}")    
                    

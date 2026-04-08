import sys

fname = input("Enter the file name: ")

try:
    with open(fname, 'r', encoding='utf-8') as fhand:
        # We only try to read if the open succeeds
        count = 0
        for line in fhand:
            count += 1
        print(f"Successfully processed {count} lines.")

except FileNotFoundError:
    # Handle the error without crashing the program
    print(f"Error: The file '{fname}' does not exist. Please check the spelling.")
    sys.exit() # Cleanly terminates the script
except PermissionError:
    print(f"Error: You do not have permission to access '{fname}'.")
    sys.exit()
    
# Path errors

from pathlib import Path

# 1. Define folder and file (The '/' operator handles the slashes for you)
folder = Path("python_pro_files")
file_to_open = folder / "mbox-short.txt"

# 2. THE PATH GUARDIAN
if file_to_open.exists() and file_to_open.is_file():
    with file_to_open.open(encoding='utf-8') as f:
        # Read just the first line to prove it works
        print(f"Success! First line: {f.readline().rstrip()}")
else:
    # 3. Graceful Failure
    print(f"Error: Could not find the file at {file_to_open.absolute()}")
    
    
# Extracting emails and saving them to a new file
with open('mbox-short.txt', 'r') as fhand:
    with open('email_list.txt', 'w', encoding='utf-8') as fout:
        for line in fhand:
            if line.startswith('From: '):
                email = line.split()[1]
                # You MUST manually add the \n
                fout.write(email + '\n')         
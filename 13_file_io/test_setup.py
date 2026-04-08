import os

if os.path.exists('mbox-short.txt'):
    print("System Ready: File detected.")
    print(f"File Size: {os.path.getsize('mbox-short.txt')} bytes")
else:
    print("Error: File not found.")
    print(f"Current Working Directory: {os.getcwd()}")
    
def process(line):
    # This is the "Happy Path" - only called if data is valid
    words = line.split()
    print(f"Processing email from: {words[1]}")

try:
    with open('mailbox.txt', 'r', encoding='utf-8') as fhand:
        for line in fhand:
            line = line.rstrip()
            
            # --- THE GUARDIANS (The "Bouncers") ---
            
            # 1. EMPTY GUARD: Skip blank lines
            if not line:
                continue
            
            # 2. ANCHOR GUARD: Must start with 'From '
            if not line.startswith('From '):
                continue

            # 3. STRUCTURE GUARD: Must have at least two parts
            # This prevents an IndexError when accessing words[1]
            words = line.split()
            if len(words) < 2:
                continue

            # --- THE LOGIC (The "Dance Floor") ---

            # Find domain using your slice logic
            at_pos = line.find('@')
            space_after = line.find(' ', at_pos)
            
            # Guardian against malformed emails (no @ or no space after)
            if at_pos == -1 or space_after == -1:
                continue

            domain = line[at_pos + 1 : space_after]
            print(f"Extracted Domain: {domain}")

            # Safe to pass to our external function now
            process(line)

except FileNotFoundError:
    print("Error: 'mailbox.txt' not found.")
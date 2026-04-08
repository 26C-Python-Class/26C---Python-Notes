# String methods 
word = "Python"
word.upper()
print(word)
word.capitalize()


# Search and counting methods
word = 'pineapple'
word.find('a')# searches a substring and returns the index of the first occurrence as an integer
word.count('e')# counts how many times a substring appears in a string

# Cleaning methods
word.strip()# Removes white spaces on both left and right of a string
word.lstrip()#removes white spaces from the left
word.rstrip()#removes white spaces from the right

username = " \n myname123 \t"
cleaned = username.strip()
print(f"'{cleaned}'")

# Data parsing
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

# Step 1: Find the @
at_position = data.find('@')
print(at_position) # 21

# Step 2: Find the first space AFTER the @
# Notice we tell find() to start searching at 'at_position'
space_position = data.find(' ', at_position)
print(space_position) # 31

# Step 3: Slice it
# We add 1 to at_position because we don't want the '@' itself
host = data[at_position + 1 : space_position]
print(host) # 'uct.ac.za'

log_entry = "2026-03-25 10:00:AM - ALERT: Product [XJ-900] was purchased for $199.99 via Stripe"

# Step 1: Find the boundaries of the Product Code
start_bracket = log_entry.find('[')
end_bracket = log_entry.find(']')

# Step 2: Slice the Product Code
# We add 1 to start_bracket to skip the '[' character itself
product_code = log_entry[start_bracket + 1 : end_bracket]

# Step 3: Find the Price
# We look for the '$' and then the next space after it
price_start = log_entry.find('$')
price_end = log_entry.find(' ', price_start)

# Step 4: Slice the Price
price = log_entry[price_start + 1 : price_end]

print(f"Product: {product_code}") # Output: XJ-900
print(f"Price: {price}")           # Output: 199.99

# Formatting strings
price = 12900.8475
# :.2f means "Fixed-point, 2 decimal places"
# :, means "Add a comma as a thousands separator"
print(f"The total is ${price:,.2f}") 
# Output: "The total is $12,900.85" (Notice it rounded!)

# The guardian pattern 
def process_order(user_id, cart, database):
    """
    Demonstrates Type, Empty, and Existence Guardians.
    """
    # 1. TYPE CHECK: Is the database actually a dictionary?
    if not isinstance(database, dict):
        return "Guard Triggered: Database is corrupted or wrong format."

    # 2. EXISTENCE CHECK: Does this user even exist?
    if user_id not in database:
        return f"Guard Triggered: User ID {user_id} not found."

    # 3. EMPTY CHECK: Is there anything to buy?
    if not cart:
        return "Guard Triggered: Shopping cart is empty."

    # --- HAPPY PATH (The Main Logic) ---
    user_name = database[user_id]['name']
    total_items = len(cart)
    return f"SUCCESS: Processing {total_items} items for {user_name}."

# --- DEMONSTRATION DATA ---
mock_db = {
    101: {"name": "Alice"},
    102: {"name": "Bob"}
}

# --- CLASSROOM TEST CASES ---
print("--- Running Guardian Demonstrations ---")

# Case A: Fails Existence Check
print(f"Test 1 (Invalid ID): {process_order(999, ['apple'], mock_db)}")

# Case B: Fails Empty Check
print(f"Test 2 (Empty Cart): {process_order(101, [], mock_db)}")

# Case C: Fails Type Check
print(f"Test 3 (Bad DB Type): {process_order(101, ['apple'], 'NotADatabase')}")

# Case D: Passes all Guardians (The Happy Path)
print(f"Test 4 (Valid Order): {process_order(101, ['apple', 'banana'], mock_db)}")


# Try except
def simple_divide():
    try:
        # 1. The "Dangerous" Code
        number = int(input("Enter a number to divide 10 by: "))
        result = 10 / number
        print(f"The answer is {result}")
        
    except:
        # 2. The "Safety Net"
        # This runs if ANY error happens above
        print("Oops! Something went wrong. Check your input.")

# Call the function
simple_divide()
# Try except and finally

def safe_divide():
    """
    Prompts the user for a number and divides 10 by it,
    handling common errors gracefully.
    """
    try:
        # Code that might cause an error
        user_input = input("Enter a number: ")
        number = int(user_input)
        result = 10 / number
        
    except ZeroDivisionError:
        # Runs ONLY if you divide by zero
        print("Error: You can't divide by zero!")
        
    except ValueError:
        # Runs ONLY if the input wasn't a number
        print(f"Error: '{user_input}' is not a valid number!")
        
    except Exception as e:
        # Catch-all for any other unexpected errors
        print(f"Something else went wrong: {e}")
        
    else:
        # Runs ONLY if the 'try' block was successful
        print(f"Success! 10 divided by {number} is {result}")
        
    finally:
        # ALWAYS runs, no matter what happened above
        print("Execution complete. Cleaning up resources...\n")

# Now you can call the function whenever you need it:
safe_divide()
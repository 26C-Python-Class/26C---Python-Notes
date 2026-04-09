def simple_division():
    try:
        # Handling dangerous code
        number = int(input("Please enter a number to divide by ten\n"))
        result = 10 / number
        print(f"The answer is {result}")
    except ZeroDivisionError:
        # Handle the errors
        print("Oops! cannot divide the number")    
    except ValueError:
        # Handle the errors
        print(f"Error: '{number}' is not valid") 
    except Exception as e:
        print(f"Something went wrong: {e}")       
        
simple_division()        
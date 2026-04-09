first_name = ''
last_name = ''

def register():
    """This is a function that registers users.
        Takes in the first name and last name.
    """  
    input("Please enter your first name...\n")
    print()
    input("Please enter your last name...\n")
    # print(f"You are noe registered ", first_name, last_name )
    return first_name, last_name
register()# Call the function    

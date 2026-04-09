def calculate_grade(score):
    """A function that calculates grades based inputted scores"""
    if score > 100 or score < 0:
        return "Invalid score"
    
    # Conditional logic for grading A, B, C, D, E 
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "E"
    
try:
    user_score = float(input("Enter the student's score: \n"))
    grade = calculate_grade(user_score)  
    print(f'Your grade is: {grade}') 
except ValueError:
    print("Please enter a valid score")     
    
    
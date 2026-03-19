import os

# Full roadmap mapping: Folder Name -> [Learning Objectives, Code Template]
roadmap = {
    "01_basics": ["Variables, snake_case, and Data Types", "name = 'Grace'\nage = 25\nprint(f'{name} is {age} years old.')"],
    "02_operators": ["Arithmetic (PEMDAS), Comparison, and Logic", "result = (10 + 5) * 2\nprint(f'Logic Check: {result > 20 and True}')"],
    "03_input_output": ["Capturing input and f-string formatting", "user = input('Name: ')\nprint(f'Hello, {user}!')"],
    "04_control_flow": ["if/elif/else and Boolean logic", "if 10 > 5:\n    print('Logic works!')"],
    "05_lists_tuples": ["Ordered collections and Mutability", "fruits = ['apple', 'banana']\nprint(fruits[0])"],
    "06_dictionaries_sets": ["Key-Value pairs and Unique collections", "user = {'id': 1, 'name': 'Admin'}\nprint(user['name'])"],
    "07_loops": ["For/While loops and Iteration", "for i in range(5):\n    print(f'Iteration {i}')"],
    "08_comprehensions": ["Pythonic List & Dict comprehensions", "squares = [x**2 for x in range(10)]"],
    "09_functions": ["Def, Return, and Parameters", "def greet(n):\n    return f'Hi {n}'"],
    "10_scope": ["LEGB Rule (Local, Global scope)", "x = 'global'\ndef check():\n    y = 'local'"],
    "11_error_handling": ["Try/Except/Else/Finally", "try:\n    x = 1/0\nexcept ZeroDivisionError:\n    print('Safe!')"],
    "12_modules_packages": ["Importing and Pip", "import math\nprint(math.sqrt(16))"],
    "13_file_io": ["Reading/Writing with Context Managers", "with open('test.txt', 'w') as f:\n    f.write('Hello World')"],
    "14_oop_basics": ["Classes, Objects, and __init__", "class Dog:\n    def __init__(self, name):\n        self.name = name"],
    "15_oop_advanced": ["Inheritance and Polymorphism", "class Robot(Dog): pass"],
    "16_decorators_generators": ["Advanced function behavior", "def my_decorator(func):\n    pass"],
    "17_testing": ["Unit testing with pytest", "def test_math():\n    assert 1 + 1 == 2"],
    "18_environments": ["Virtual Environments (venv)", "# No code here, use terminal commands"],
    "19_apis_web": ["Requests and JSON data", "import requests\n# response = requests.get(...)"],
    "20_database": ["SQLite3 and SQL queries", "import sqlite3\nconn = sqlite3.connect(':memory:')"]
}

def build_clean_repo():
    for folder, content in roadmap.items():
        if not os.path.exists(folder):
            os.makedirs(folder)
            
        # 1. Create Module README (No Emojis)
        with open(os.path.join(folder, "README.md"), "w", encoding="utf-8") as f:
            module_title = folder.split('_', 1)[1].replace('_', ' ').title()
            f.write(f"# Module: {module_title}\n")
            f.write(f"Focus: {content[0]}\n\n")
            f.write("Status: [ ] Planned | [-] In Progress | [X] Complete\n\n")
            f.write("## Goals\n- Understand core syntax\n- Complete starter lab\n- Pass module check\n")

        # 2. Create Starter Script
        with open(os.path.join(folder, "lab.py"), "w", encoding="utf-8") as f:
            f.write(f'"""\nStarter Lab: {folder}\n"""\n\n')
            f.write(content[1])
            
        print(f"Created: {folder}/")

if __name__ == "__main__":
    build_clean_repo()
    print("\nRoadmap structure initialized successfully.")
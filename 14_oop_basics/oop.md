# Comprehensive Teaching Guide: Python Object-Oriented Programming (OOP)

This guide is designed to take you from the fundamental "blueprint" mental model to the professional implementation of the Four Pillars of OOP.

---

## 1. The Core Philosophy: Blueprints vs. Buildings
Object-Oriented Programming is about grouping **data** (attributes) and **behavior** (methods) into reusable units.

* **Class:** The architectural blueprint. It defines what a "House" should have (windows, doors) but isn't a house itself.
* **Object (Instance):** The actual house built from the blueprint. It has a specific color, address, and owner.



---

## 2. Core Concepts & Syntax

### Attributes: Storing Data
Attributes are variables that belong to a class or an instance.

| Attribute Type | Scope | Definition |
| :--- | :--- | :--- |
| **Class Attribute** | Shared by **all** instances. | Defined directly in the class body. |
| **Instance Attribute** | Unique to **each** instance. | Defined inside the `__init__` method using `self`. |

### Methods: Defining Behavior
Methods are functions defined inside a class. They always take `self` as the first argument, representing the specific object calling the method.

```python
class Dog:
    # Class Attribute (Global to all dogs)
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance Attributes (Unique to each dog)
        self.name = name
        self.age = age

    # Instance Method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Instantiating (Creating objects)
buddy = Dog("Buddy", 9)
print(buddy.speak("Woof")) # Buddy says Woof
```

---

## 3. The Four Pillars of OOP
These concepts allow us to manage complexity in large systems.

### I. Encapsulation (Data Privacy)
Encapsulation bundles data and methods while protecting internal states. In Python, we use a single underscore `_` (protected) or double underscore `__` (private) to signal that a variable shouldn't be touched directly.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute (Double underscore)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")

    def get_balance(self):
        return f"Account Holder: {self.owner} | Balance: {self.__balance}"

account = BankAccount("Kwanusu", 1000)
account.deposit(500)
# print(account.__balance)  # This would throw an AttributeError
print(account.get_balance())
```



[Image of encapsulation in object-oriented programming]


### II. Inheritance (Code Reuse)
Inheritance allows a "Child" class to derive attributes and methods from a "Parent" class.

```python
class Animal:
    def eat(self):
        print("Munch munch...")

class Cat(Animal): # Inherits from Animal
    def meow(self):
        print("Meow!")

my_cat = Cat()
my_cat.eat() # Inherited method


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return f"{self.name} is working."

class Developer(Employee):
    # Inherits everything from Employee
    def code(self):
        return f"{self.name} is writing TypeScript."

dev = Developer("Alice", 80000)
print(dev.work()) # Inherited method
print(dev.code()) # Subclass-specific method
```

### III. Polymorphism (Multiple Forms)
Polymorphism allows different classes to share the same method name but behave differently. This is often achieved via **Method Overriding**.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.10  # Standard 10% bonus

class LeadArchitect(Employee):
    def calculate_bonus(self):
        return self.salary * 0.25  # Overridden: 25% bonus for architects

staff = [Employee("Bob", 5000), LeadArchitect("Joseph", 7000)]

for person in staff:
    # The same method call behaves differently based on the object type
    print(f"{person.name} Bonus: {person.calculate_bonus()}")
```



### IV. Abstraction (Complexity Hiding)
Abstraction hides the "how" and shows only the "what." A user knows how to use a `RemoteControl` (press 'On'), but they don't need to know the electrical circuitry inside.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        # Every shape MUST have an area, but the formula differs
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

# shape = Shape() # This will fail (cannot instantiate an abstract class)
my_square = Square(5)
print(f"Square Area: {my_square.area()}")
```

---

## 4. Special Methods (Dunder Methods)
"Dunder" stands for **D**ouble **Under**score. These methods allow your objects to interact with Python's built-in functions.

* `__init__(self, ...)`: The **Constructor**. Runs automatically when an object is created.
* `__str__(self)`: What the user sees when calling `print(object)`.
* `__repr__(self)`: What the developer sees during debugging.

```python
class Task:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Task: {self.title}"

todo = Task("Complete API Docs")
print(todo) # Output: Task: Complete API Docs


class Project:
    def __init__(self, title, technology):
        self.title = title
        self.technology = technology

    def __str__(self):
        # Informal, user-friendly string
        return f"Project: {self.title} ({self.technology})"

    def __repr__(self):
        # Official, developer-friendly string
        return f"Project(title='{self.title}', technology='{self.technology}')"

p1 = Project("Smart Print Shop", "React & Django")
print(str(p1))   # For the user
print(repr(p1))  # For the logs/debugger
```

---

## 5. Summary Table

| Concept | Purpose | Analogy |
| :--- | :--- | :--- |
| **Encapsulation** | Security/Safety | A capsule pill (contents are hidden). |
| **Inheritance** | Reuse | Genetics (you get traits from parents). |
| **Polymorphism** | Flexibility | A "Play" button (works on music, video, or games). |
| **Abstraction** | Simplicity | Driving a car (you don't need to be a mechanic). |

"""Question 1 — Class & Object Creation
Write a Python class Book with attributes title and author.
Then:

Create two objects with different values.

Print their details in the format:"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("GOT", "ABinash")
book2 = Book("Sasha and Bear", "Anvika")

print(f"Book1: {book1}, Author: {book1.author}")
print(f"Book2: {book2}, Author: {book2.author}")


"""2. Constructor Behavior
Question:
Modify the Book class so that if the author is not provided, it defaults to "Unknown"."""
class Book:
    def __init__(self, title, author=None):
        self.title = title
        self.author = author if author is not None else "Unknown"

book3 = Book("Mission Impossible")
print(f"Book3: {book3}, Author: {book3.author}")


"""3. Instance vs Class Variables
Question:
Create a Student class with:

Class variable school_name (default "ABC School")

Instance variable name
Change school_name for one instance only and explain the output."""
class Student:
    school_name = "ABC School"

    def __init__(self, name):
        self.name = name

s1 = Student("Shiro")
s2 = Student("Nakito")

# change studen1 class name
Student.school_name = "Little Angel"
print(f"School Name for {s1.name}: {s1.school_name}")
print(f"School Name for {s2.name}: {s2.school_name}")

# change student2 class name
s2.school_name = "ABC School"
print(f"School Name for {s2.name} after updating instance variable: {s2.school_name}")


"""4. Encapsulation
Question:
Make a BankAccount class where balance is private.

Add a method to deposit money

Add a method to view the balance
Try to change the balance directly from outside and explain what happens."""

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

a1 = BankAccount(100)
a1.deposit(200)
print("Current Balance is:", a1.get_balance())
a1.__balance = 999
print("Balance:", a1.get_balance())
print(a1.__dict__) # Python name-mangles private attributes like __balance: creates a new public attribute __balance on the object, leaving the real balance untouched.


"""5. Inheritance
Question:
Create a base class Shape with a method area().
Create subclasses Rectangle and Circle that override area() with correct formulas."""
import math
class Shape():
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
r1 = Rectangle(10,4)
c1 = Circle(4)
print(f"Area of Rectangle: {r1.area()} and Circle: {c1.area()}")


"""6.Create a function make_it_speak(animal) that takes any object and calls its speak() method.

Create two unrelated classes:

Dog with speak() → "Woof"

Robot with speak() → "Beep Boop"

Pass objects of both classes to make_it_speak() and show that it works without inheritance."""
def make_it_speak(animal):
    if hasattr(animal, "speak") and callable(animal.speak):
        return animal.speak()
    else:
        return "this object can not speak"

class Dog:
    def speak(self):
        return "Woof"

class Robot:
    def speak(self):
        return "Beep Beep" 

class Bottle:
    pass
    
print(make_it_speak(Dog()))
print(make_it_speak(Robot()))
print(make_it_speak(Bottle()))


"""7. Method Overloading (Python-style)
Question:
Python doesn’t have traditional method overloading.
Write a class Calculator where add() can handle both:

add(2, 3)

add(2, 3, 4)"""

class Calculator:
    def add(self, *args):
        if all(isinstance(x, (int, float)) for x in args):
            return sum(args)
        else:
            return "Numbers provided are not numeric type."
        
        
c1 = Calculator()
print(c1.add(2,3))
print(c1.add(2,13,9))
print(c1.add("a", 3,4))


"""8. Method Overriding
Question:
Create a base class Vehicle with method start().
Create a subclass Car that overrides start() but still calls the parent’s start() inside it."""
# from abc import ABC, abstractmethod
class Vehicle:
    #@abstractmethod # this is required in case if we just need boilerplate in base class and implementation in sub class.
    def start(self):
        return "Vehicle initializing..."

class Car(Vehicle):
    def start(self):
        parent_msg = super().start()
        return f"{parent_msg} Car engine started."
    
c = Car()
print(c.start())


"""9. Static vs Class Methods
Question:
Create a class MathUtils with:

Static method is_even(number)

Class method change_pi(value)

Class variable pi
Show how static and class methods differ in usage."""
import math
class MathUtils:
    pi = math.pi

    @staticmethod
    def is_even(number):
        return number % 2 == 0

    @classmethod
    def change_pi(cls, value):
        cls.pi = value
        return cls.pi
    
mt = MathUtils()
print(mt.is_even(4))
print(mt.change_pi(3.14900))


"""10. Abstraction
Question:
Using abc module, create an abstract base class Payment with method pay(amount).
Create subclasses CreditCardPayment and PaypalPayment that implement it."""
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
            amount = amount + (amount * 2/100)
            return amount


class PaypalPayment(Payment):
    def pay(self, amount):
        amount = amount + (amount * 3.5/100)
        return amount
    
p2 = CreditCardPayment()
p3 = PaypalPayment()
print(p2.pay(30))
print(p3.pay(5530))
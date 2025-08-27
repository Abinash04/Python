# Interview OOPs Questions (Practical)

# Class & Objects
# Create a Car class with attributes brand and model. Write a method drive() that prints "Driving <brand> <model>". Then create two objects and call the method.
class Car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"Driving {self.brand} {self.model}.")

c1 = Car("Suzuki", "Vitara")
c2 = Car("Honda", "City")
c1.drive()
c2.drive()

# Encapsulation
# Suppose you are designing a BankAccount class. The balance should not be directly accessible. Implement getters and setters to access and update balance safely.
class InsufficientFund:
    pass

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def _validate_amount(self, amount):
        if amount < 0:
            return ValueError("Amount should be positive!")
        if not isinstance(amount, (int, float)):
            return TypeError("Amount should be a number.")
        if amount > self._balance:
            return InsufficientFund("Insufficient Funds.")

    def get_balance(self):
        return self._balance
    
    def deposit_balance(self, amount):
        self._validate_amount(amount)
        self._balance += amount
        return self._balance

    def withdraw_balance(self, amount):
        self._validate_amount(amount)
        self._balance -= amount
        return self._balance

b1 = BankAccount(100)
b1.get_balance

# Inheritance
# Create a Shape class with a method area(). Derive Rectangle and Circle classes from it and override the area() method.
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def area(self, length, breadth):
        return 2 * (length * breadth)
    
class Circle(Shape):
    def area(self, radius):
        return 3.14 * radius **2

# Polymorphism
# Write two classes Dog and Cat, each having a speak() method. Write a function animal_sound() that takes any object and calls speak(). Show how polymorphism works.
class Dog:
    def speak(self):
        return "Bow Bow"
    
class Cat:
    def speak(self):
        return "Meow Meow"

def animal_sound(animal_obj):
    return animal_obj.speak()
   
d1 = Dog()
c1 = Cat()
print(animal_sound(d1))
print(animal_sound(c1))

# Abstraction
# Use Python’s abc module to create an abstract class Vehicle with an abstract method start_engine(). Then implement it in Car and Bike.
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return f"{self.__class__.__name__} started."

class Bike(Vehicle):
    def start_engine(self):
        return f"Bike started."

# Operator Overloading
# Define a Vector class that overloads the + operator so that you can add two vectors like v1 + v2.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return (self.x + other.x, self.y + other.y)

v1 = Vector(10, 12)
v2 = Vector(110, 121)
v3 = Vector(130, 17)
print(v1 + v2)
# print(v1 + v2 + v3)

# Method Overloading vs Method Overriding
# Python doesn’t support method overloading natively. How would you implement a class Calculator that handles both add(2,3) and add(2,3,4)?
class Calculator:
    def add(self, *args):
        return sum(args)
    
c1 = Calculator()
print(c1.add(2,3))
print(c1.add(2,3,4))

# Composition vs Inheritance
# Create a Engine class and a Car class. Show an example where the Car has-a Engine instead of inheriting from it.

class Engine:
    pass

class Car:
    def __init__(self):
        self.engine = Engine()



# Class vs Static Methods
# Write a class MathUtils with:

# a @staticmethod for calculating factorial

# a @classmethod for returning an instance with a pre-defined number.

class MathUtils:
    def __init__(self, number=None):
        self.number = number

    @staticmethod
    def factorial(value):
        return value * 2
    
    @classmethod
    def pre_defined_number(cls, value):
        return cls(value)

m = MathUtils(10)
obj = m.pre_defined_number(23)
print(obj.number)

# Multiple Inheritance & MRO (Method Resolution Order)
# Create two parent classes A and B both with a method greet(). Then create a child class C(A,B) and call greet(). Explain which one is called and why.
class A:
    def greet(self):
        return "INside A"

class B:
    def greet(self):
        return "INside B"

class C(A,B):
    def __init__(self):
        self.greet()

    def greet(self):
        return "INside C"

    def __str__(self):
        return f"{self.greet()}"

c = C()
print(c)

"""Check if we can use any other keyword apart from self in a class."""
class Sports:
    def __init__(this, name):
        print("First init")
        this.name = name

    def __init__(this, name):
        print("Second init")
        this.name = name

    def __str__(this):
        return f"Sports Class - {this.name}"

s = Sports("Football")
print(s)

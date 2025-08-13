#################################################################################
# 10 practical, code-writing OOP questions that collectively test:

# Abstraction

# Encapsulation

# Inheritance (single, multiple, multilevel)

# Polymorphism (overloading, overriding)

# Method resolution order (MRO)

# Static/class methods

# Special methods (__str__, __repr__, __eq__, etc.)

# Property decorators

# Composition vs inheritance

# Interfaces and abstract classes"""

# """10 Practical Python OOP Questions
# (Answer each with actual Python code, not just explanations)
############################################################################

"""Q1. Abstraction & Interface
Create an abstract base class Shape with:

An abstract method area()

An abstract method perimeter()
Implement two concrete classes Rectangle and Circle that inherit from Shape and implement both methods."""
from abc import ABC, abstractmethod
import math
from dataclasses import dataclass
class Shape(ABC):
    """Abstract base class for different types of shapes."""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def _validate_positive_number(self, name, value):
        """protected helper method to check for positive numbers"""
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be numeric!")
        if value <= 0:
            raise ValueError(f"{name} provided should be positive!")

@dataclass
class Rectangle(Shape):
    """Rectangle class to calculate area and perimeter."""
    length: float
    breadth: float

    def __post_init__(self):
        self._validate_positive_number("Length", self.length)
        self._validate_positive_number("Breadth", self.breadth)
        
    def area(self):
        return round(self.length * self.breadth, 2)

    def perimeter(self):
        return round(2 * (self.length + self.breadth), 2)

@dataclass
class Circle(Shape):
    """Circle class to calculate area and perimeter."""
    radius: float

    def __post_init__(self):
        self._validate_positive_number("Radius", self.radius)

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

length = 120
breadth = 34
radius = 29
shapes = [Rectangle(length,breadth), Circle(radius)]
for shape in shapes:
    name = shape.__class__.__name__
    print(f"{name}-> Area: {shape.area()}, {name}-> Perimeter: {shape.perimeter()}")




"""Q2. Encapsulation
Create a BankAccount class where:

The balance is private.

You can deposit and withdraw money.

You can check balance using a method, but you cannot directly modify the balance.

Attempting to withdraw more than balance should raise a custom exception InsufficientFunds."""

class InsufficientFundsError(Exception):
    pass

class BankAccount:
    """BankAccount class to show the balance funds."""
    def __init__(self, balance):
        self.__balance = balance

    def _validate_positive_balance(self, name, value):
        if not isinstance(value, (int,float)):
            raise TypeError(f"{name} should be numeric!")
        
        if value <= 0:
            raise ValueError(f"{name} should be positive!")

    def get_balance(self):
        return f"Current Balance:{self.__balance}"
    
    # dunder method - double underscore
    def __str__(self):
        return f"BankAccount with balance:{self.__balance}"

    def withdraw(self, amount):
        self._validate_positive_balance("Withdraw", amount)
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            raise InsufficientFundsError(f"Not enough funds to withdraw!")
        return f"Withdrawn: {amount},  {self.get_balance()}"


    def deposit(self, amount):
        self._validate_positive_balance("Deposit", amount)
        self.__balance += amount
        return f"Deposited: {amount},  {self.get_balance()}"
    
    
acc = BankAccount(2000)
print(acc)
print(acc.withdraw(100))
print(acc.deposit(200))
print(acc.withdraw(210))
acc.__balance = 99999
print(acc.get_balance())
print(acc.__dict__)


"""Q3. Single Inheritance & Overriding
Create a Vehicle class with a max_speed and mileage attributes, and a display() method.
Create a subclass Car that overrides display() to include an extra attribute seats."""
from dataclasses import dataclass
@dataclass
class Vehicle:
    max_speed: int
    mileage: int

    def display(self):
        return f"Car max speed: {self.max_speed} km/hr and mileage: {self.mileage}/litre"

@dataclass
class Car(Vehicle):
    seats: int

    def display(self):
        base_info = super().display()
        return f"{base_info} and has {self.seats} seats!"
    

c1 = Car(160,16,4)
print(c1.display())


"""Q4. Multiple Inheritance & MRO
Create two classes Electric and Petrol both having a fuel_type() method.
Create a HybridCar class that inherits from both and resolves ambiguity using MRO.
Show the HybridCar's MRO."""
class Electric:
    def fuel_type(self):
        return f"Fuel Type: Electric"

class Petrol:
    def fuel_type(self):
        return f"Fuel Type: Petrol"

class HybridCar(Electric, Petrol):
    def fuel_type(self):
        electricity_type = super().fuel_type()
        petrol_type = Petrol.fuel_type(self)
        return f"MRO: electricity - {electricity_type}, petrol - {petrol_type}"

print(HybridCar.__mro__)
print(HybridCar.mro())
print(HybridCar().fuel_type())


"""Q5. Class vs Instance vs Static Methods
Create a MathOps class with:

A @classmethod called from_string that takes a string "3,4" and returns a MathOps instance with two numbers.

A @staticmethod called is_even that checks if a number is even.

A normal instance method add that returns the sum of the two numbers."""


class MathOps:
    """A class to check all types of methods"""

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    @classmethod
    def from_string(cls, str1):
        num1, num2 = map(int, str1.split(","))
        return cls(num1, num2)

    @staticmethod
    def is_even(value):
        return value % 2 == 0

    def add(self):
        return self.num1 + self.num2
    

m = MathOps.from_string("4,9")
print(m.is_even(9))
print(m.add())

# Q6. Operator Overloading
# Create a Point class with x and y attributes.
# Overload the + operator to add two points, and the == operator to compare them.

# Q7. Property Decorators
# Create a Temperature class where:

# celsius is stored internally.

# You can get and set fahrenheit using @property and setter methods.

# Setting fahrenheit updates the celsius value automatically.

# Q8. Composition vs Inheritance
# Create:

# A Battery class with a method battery_info().

# An Engine class with a method engine_info().

# A Car class that uses composition to include both a battery and engine, instead of inheriting from them.

# Q9. Polymorphism
# Create an abstract Payment class with an abstract pay() method.
# Implement CreditCardPayment and UPIPayment that process payments differently.
# Write a function process_payment(payment_obj, amount) that works with any payment method.

# Q10. Dunder Methods & String Representation
# Create a Book class with attributes title and author.
# Implement:

# __str__ to print "Title by Author".

# __repr__ to return "Book(title='...', author='...')"."""
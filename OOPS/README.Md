Object will have behavior.
Attributes - variables
Behaviors - methods

Different between methods and functions.
- Methods belong to a class
- function in OOP is called an methods.

Example:
Phone ,
designed - Motorola
manufactured -India
where it has been designed owns the product.

design or blueprint is called the class.
class - design
object - instance

if you have design you can create multiple objects from that design, here in this example-
if you have the phone design then you can create multiple phones of the same design from anywhere.

if you want to build an object then need to build a class.

builtin type - int , float, string

custom class like below:
class Computer:
Attributes - Variables
Behaviors - Methods

class Computer:

    def __init__(self, cpu, ram):

    def config(self):
        print("i5, 16gb, 1TB")


python dynamic type - 
a = 8 -> int
a= '9' -> string

com1 = Computer() # object of Computer
type(com1) # <class '__main__.Computer'>

Computer.config() # error - coz # hey human walk - which human? who should walk? Guddu walk
Computer.config(com1) # it works

com2 = Computer()
Computer.config(com2)

com1.config() # works , behind the scene config will take com1 as argument. self is the object which we are passing.
 
 __init__ - special method - will be called for every object, it will instanstiate. also a constructor

 heap memory - object will take some space, every space will have address.
 print(id(com1))

 different obj will take diff address in heap space.
 who will decide and allocate the memory - 
 size of an object -> depends on the number of variables and size of each variable
 who allocates size to object?

 constructor will decide memory and size.

 self:
 even if yu have 10 objects then current object being worked upon will be referred in the self object

 comparing 2 objects.
 def compare(self, c2):

 Variables Types:
 Instance
 Class
 
 Class Student:
    school = "NMIT" # Class or static variable.

    def __init__(self):
        self.age = age;  # instance variables are separate for different objects
        self.name = name; # instance variables

Class variables will affect all the object.

Student.school = "IJCT" # it will change the school for all the Student objects.

Namespace; - 
Class and Instance

variables to store data and methods for behaviors.

Types of Methods:
Instance
Class
Static

class Student:
    school = 'NMIT' # to work with class variable , you can use class methods.

    def __init__(self, m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self): # instance methods, works with objects , 2 types of instance- accessors and mutators
        return (self.m1 + self.m2 +self.m3) / 3

    def get_m1(self):
        return self.m1
    
    def set_m1(self,value):
        self.m1 = value

    @classmethod # decorator
    def getSchool(cls): # class method-  to call class method we need to use special symbol called as decorators.
        return cls.school
    
    @staticmethod
    def info(): ## keep it blank , static method, need to use special decorator, nothing to do with class or instance variables.

    

s1 = Student(10,45,23)
s2 = Student(23,45,67)

s1.get_m1(23) # instance method
Student.getSchool() # error if we dont use the line#114 i.e. decorators. # class method
Student.info() # static method


Accessors: 
fetch the value of instance variables, getter methods
Mutators:
sets the value, setter methods.

Inner class in Python:
class within a class.

class Student: # outer class
    def __init__(self, name, rollno): # constructor
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop() // creating inner class object

    def show(self, name, rollno): # to print the details of the student
        print(self.name, self.rollno)
        self.lap.show() # to print the details if the students wth

    class Laptop: # inner class
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = '8gb'

        def show(self):
            print(self.brand, self.cpu, self.ram)
    
s1 = Student('Abi',123)
s2 = Student('Som',345)

lap1 = Student().Laptop() # create obj of inner class in the outer class or create obj of innef class outside of outer class but by using outer class name to call it.
s1.show()

 to print details of s1 we need to call print(s1.name, s1.rollno)
 instead of doing this we can create a method to show all the details for any given student.


Inheritance:

class A: # parent class
    def feature1(self):
        print("Feature1 working)
    
    def feature2(self):
        print("Feature2 working)

class B(A): # child class # single level inheritance
    def feature3(self):
        print("Feature3 working)
    
    def feature4(self):
        print("Feature4 working)


class C(B): # child class # multi-level inheritance
    def feature3(self):
        print("Feature3 working)

a1 = A()
a1.feature1()
a1.feature2()

# get the feature of A as well from B, class B is inherting the features from A
b1 = B()
b1.feature1() # inheriting the feature from super class A.


Multi-level inheritance:
class C will derive from class B which in turn derives the features from class A.


class C(A,B): # multiple inheritance
class C can inherit feaures from A and B.


sub class can access all the features of super class but not vice-versa.

Constructors in inheritance:
 
class A:

class B(A):

a1 = A() # constructor

a1 = B() 
In case if we do not have __init__ in class B so it goes to the __init__ from class A and in case class B has the method then the __init__ will be printed, the flow goes from B->A
if __init__ is present in B then prints the B else if its present in A then prints the A.

In case if we want to access the instance variables of super class within the child class __init__ method then we can use the keyword super.

class A:
    def __init__(self):

class B(A):
    def __init__(self);
        super().__init__() # to call the super class A's init


class C(A,B):
    def __init__(self):
        super().__init__() #even though the inheritance is from A and B but due to MRO, its always the left side which will be given preference, so A's __init__ will be called.

a1 = C()
a1.feature1()

 Method resolution order; MRO
 left to right
    C
    /\
   A  B


Polymorphism:

Many forms.
obj can have multipel forms.
4 ways of polymorphism:
duck typing
operator overloading
method overloading
method overriding

Duck typing:
 doesn't matter which object but should have the same method
x = 5
x = 'Abi'

class PyCharm:
    def execute(self):
        print("compiling")
        print("running")

class MyEditor:
    def execute(self):
        print("Spell check")
        print("convention check")
        print("compiling")
        print("running")


class Laptop:
    def code(self, ide):
        ide.execute()

ide = PyCharm() # type pycharm
ide = MyEditor() # type MyEditor, doesnt matter which class , only thing matters is it should have the same method, its called duck typing.
if an animal quacks like a duck, walks like a duck and swims like a duck then probably its a duck.

lap1 = Laptop()
lap1.code(ide)


Operator overloading and Polymorphism:

5 + 6 , 5 and 6 are operands and + is the operator

synthetic sugar - cant add int and str
a=5
b=6
int.__add__(a,b) # internally calling add method which belongs to int class.
st.__add__(a,b) # internally calling add method which belongs to str class.

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1+m2)

        return s3

s1 = Student(12,23)
s2 = Student(23,43)

s3 = s1 + s2 
# here we have overloaded the + operator which internally calls the __add__ method of int class. to overload we need to have the same method defined
# in the student class. same method name but arguments are of different types.

when you print the object, then it prints the address 

overriding:

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
    
    def __gt__(self, other): # this method is overriding the existing __gt__ in built method.
        r1 = self.m1 + other.m1
        r2 = self.m2 + other.m2
        if r1 > r2:
            return True
        else:
            return False

if s1> s2:
    # print something abt s1
else:
    # print abt s2


overriding:

class A:
    def show(self):
        print("in A")

class B:
    pass
    def show(self):
        print("in B") # overrides method overrding of A class.

a1 = B()
a1.show()


Abstraction:

breaking of the things. for example- classes Player, Game, City of GTA game. breaking of work into different classes.

encapsulation - to hide the details or the implementation. Aam khao guthli mat gino.
for example: how the mouse works internally -hide the internal.


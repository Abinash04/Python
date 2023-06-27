'''
https://www.w3resource.com/python-exercises/class-exercises/#basic

Python class, Basic exercises [12 exercises with solution]

1. Write a Python program to import a built-in array module and display the namespace of the said module.
'''

import array

for name in array.__dict__:
    print(name)

print("*********************************")

'''
2. Write a Python program to create a class and display the namespace of that class.
'''

class Employee:
        def __init__(self, name, age):
             self.name = name
             self.age = age
        
        def details(self, gender, org, id):
             self.gender = gender
             self.org = org
             self.id = id

emp = Employee("Abi", 33)
emp.details("M","IP",101)

for name in Employee.__dict__:
    print(name)

print("*********************************")

'''
3. Write a Python program to create an instance of a specified class and display the namespace of the said instance.
'''

class Employee:
        def __init__(self, name, age):
             self.name = name
             self.age = age
        
        def details(self, gender, org, id):
             self.gender = gender
             self.org = org
             self.id = id

emp = Employee("Abi", 33)
emp.details("M","IP",101)

for name in emp.__dict__:
    print(name)

print("*********************************")

'''
4. 'builtins' module provides direct access to all 'built-in' identifiers of Python.
Write a Python program that imports the abs() function using the builtins module, displays the documentation of the abs() function and finds the absolute value of -155.
'''

# from builtins import abs
import builtins
# help(builtins.abs)
print(builtins.abs(-155))


print("*********************************")

'''
5. Define a Python function student(). Using function attributes display the names of all arguments.
'''

def student(name, age):
     name = name
     age = age
     print(name, age)
    
print("*********************************")

'''
6. Write a Python function student_data () that will print the ID of a student (student_id). If the user passes an argument student_name or student_
class the function will print the student name and class.
'''

def student_data(student_id, **kwargs):
     print(f"student_id:{student_id}")
     if 'student_name' in kwargs:
          print(kwargs['student_name'])
     
     if 'student_class' in kwargs:
          print(kwargs['student_class'])
     
     if 'student_name' and 'student_class' in kwargs:
          print(kwargs['student_class'], kwargs['student_name'])
     
student_data(student_id=101, student_class='VA', student_name='Som')
print("*********************************")

'''
7. Write a simple Python class named Student and display its type.
 Also, display the __dict__ attribute keys and the value of the __module__ attribute of the Student class.
'''

class Student:
     pass 

s1 = Student()
print(type(s1))
print(s1.__dict__.keys)
print(s1.__module__)
print("*********************************")

'''
8. Write a Python program to create two empty classes, Student and Marks. Now create some instances and check whether they are
 instances of the said classes or not. Also, check whether the said classes are subclasses of the built-in object class or not.
'''

class Student:
     pass

class Marks:
     pass

s = Student()
m = Marks()
print(isinstance(s, Student))
isinstance(m, Marks)
print(issubclass(Student, object))
issubclass(Marks, object)
print("*********************************")


'''
9. Write a Python class named Student with two attributes student_name, marks. 
Modify the attribute values of the said class and print the original and modified values of the said attributes.
'''

class Student:

     student_name= "ABC"
     student_age = 12
     def __init__(self,student_name,marks) -> None:
          self.student_name = student_name
          self.marks = marks

     def set_name(self,name):
          self.student_name = name
          return self.student_name
     
     def set_marks(self, marks):
          self.marks = marks
          return self.marks
     
s = Student("AB", "23")
s.set_marks(34)
s.set_name("Abi")

getattr(Student, 'student_name')
setattr(Student, 'student_name', "Abinash")
getattr(Student, 'student_age')
setattr(Student, 'student_age', 15)
print("*********************************")

'''
10. Write a Python class named Student with two attributes student_id, student_name. 
Add a new attribute student_class and display the entire attribute and the values of the class. 
Now remove the student_name attribute and display the entire attribute with values.
'''

class Student:
     student_id = 1
     student_name = 'Abi'

    
     @classmethod     
     def show(cls):
          '''
          class method to show the details of the class
          '''
          # print(cls.__dict__.items())
          '''
          Output of the above line:
          dict_items([('__module__', '__main__'), ('student_id', 1), ('student_name', 'Abi'),
          ('show', <classmethod(<function Student.show at 0x7f14b11a2170>)>), 
          ('__dict__', <attribute '__dict__' of 'Student' objects>), ('__weakref__', <attribute '__weakref__' of 'Student' objects>), ('__doc__', None)])
          '''
          for attr, value in cls.__dict__.items():
               if not attr.startswith('_') and attr != 'show':
                    print(attr,value)
          return


print("Original value:")
print(Student.show())
Student.student_class = 'VI-A'
print(Student.show())
del Student.student_name
print(Student.show())
print("*********************************")

'''
11. Write a Python class named Student with two attributes: student_id, student_name. Add a new attribute: student_class. 
Create a function to display all attributes and their values in the Student class.
'''

class Student_:
     student_id = 1
     student_name = "Abinash"

     @classmethod
     def show(cls):
          for attr, value in cls.__dict__.items():
               if not attr.startswith('_') and attr != 'show':
                    print(attr, value)

Student_.show()
print("*********************************")

'''
12. Write a Python class named Student with two instances student1, student2 and assign values to the instances' attributes. 
Print all the attributes of the student1, student2 instances with their values in the given format.
'''

class Student__:
     def __init__(self, name, age) -> None:
          self.name = name
          self.age = age
          print(self.name, self.age)

s1 = Student__("Abi", 33)
s2 = Student__("Jack", 34)
print("*********************************")

'''
Python class, Real-life problems

1. Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and methods like calculate_emp_salary, emp_assign_department, and print_employee_details.
Sample Employee Data:
"ADAMS", "E7876", 50000, "ACCOUNTING"
"JONES", "E7499", 45000, "RESEARCH"
"MARTIN", "E7900", 50000, "SALES"
"SMITH", "E7698", 55000, "OPERATIONS"
Use 'assign_department' method to change the department of an employee.
Use 'print_employee_details' method to print the details of an employee.
Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, which is the number of hours worked by the employee. If the number of hours worked is more than 50, the method computes overtime and adds it 
to the salary. Overtime is calculated as following formula:
overtime = hours_worked - 50
Overtime amount = (overtime * (salary / 50))
'''

class Employee_:
     '''
     Solving above problem
     '''
     def __init__(self,emp_id, emp_name, emp_salary, emp_department) -> None:
          self.emp_id = emp_id
          self.emp_name = emp_name
          self.emp_salary = emp_salary
          self.emp_department = emp_department

     def calculate_emp_salary(self, salary, hours_worked):
          overtime_amt = 0
          if hours_worked > 50:
               overtime = hours_worked - 50
               overtime_amt = (overtime * (self.emp_salary / 50))
          self.emp_salary += overtime_amt
          return self.emp_salary
          
     
     def emp_assign_department(self, new_dept):
          self.emp_department = new_dept
          return self.emp_department

     def print_employee_details(self):
          return f"EMP_ID:{self.emp_id}, EMP_NAME:{self.emp_name}, EMP_SAL:{self.emp_salary}, EMP_DEPT:{self.emp_department}"


emp1 = Employee_("ADAMS", "E7876", 50000, "ACCOUNTING")
emp2 = Employee_("JONES", "E7499", 45000, "RESEARCH")
emp3 = Employee_("MARTIN", "E7900", 50000, "SALES")
emp4 = Employee_("SMITH", "E7698", 55000, "OPERATIONS")
print(emp1.print_employee_details())
emp2.emp_assign_department("IT")
print(emp2.print_employee_details())
print(emp2.calculate_emp_salary(50000, 51))
print(emp2.print_employee_details())


'''
2. Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders, and methods like add_item_to_menu, book_tables, and customer_order.
Perform the following tasks now:
Now add items to the menu.
Make table reservations.
Take customer orders.
Print the menu.
Print table reservations.
Print customer orders.
'''

class Restaurant:
     def __init__(self):
          self.menu_items = {}
          self.book_table = []
          self.customer_orders = []

     
     def add_item_to_menu(self, item, price):
          self.menu_items[item] = price
     
     def book_tables(self, table_num):
          self.book_table.append(table_num)
     
     def customer_order(self, table_num, order):
          order_details = {table_num: order}
          self.customer_orders.append(order_details)

     def print_menu(self):
          for item, price in self.menu_items.items():
               print(item, price)

     def print_table_reservations(self):
          for table in self.book_table:
               print(table)
     
     def print_customer_orders(self):
          for order in self.customer_orders:
               print(order)

res = Restaurant()
res.add_item_to_menu("Biryani", 200)
res.add_item_to_menu("Pizza", 300)
res.add_item_to_menu("Salad", 100)
res.add_item_to_menu("Chicken Tikka", 190)
res.add_item_to_menu("Vegan", 180)
res.book_tables(1)
res.book_tables(2)
res.book_tables(3)
res.book_tables(4)

res.print_menu()
res.customer_order(1, "Pizza")
res.customer_order(1, "Vegan")
res.customer_order(2, "Salad")
res.print_table_reservations()
res.print_customer_orders()
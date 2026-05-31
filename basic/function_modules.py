##exploring two fundamental concepts in Python programming: functions and modules.

#Defining and Using Functions   
def greet(name):
    return f"Hello, {name}!"

#running the function created above , in this case greet function.
#refer to screenshot pss32 in readme.md for result
result = greet("Alice")
print(result)

#function is useful because i dont need to rewrite the code again ,eg greeting multiple people, instead of rewriting the fstring i can simply 
use the greet function and replace the name i want and it will return HELLO,{name}

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet("Bob"))
print(greet("Charlie"))

#create a function that performs calculation
def calculate_area(length, width):
    return length * width

area = calculate_area(5, 3)
#refer to screenshot pss33 in readme.md for result
print(f"The area is: {area}")

#returning multiple values using tuples
def min_max(numbers):
    return min(numbers), max(numbers)

#set 2 separate variable to receive two different value.
minimum, maximum = min_max([1, 5, 3, 9, 2])
#refer to screenshot pss34 in readme.md for result
print(f"Minimum: {minimum}, Maximum: {maximum}")

#function scope
#exploring global and local variable
x = 10  # Global variable

def print_x():
    print(f"Global x: {x}")

print_x()

def change_x():
    x = 20  # Local variable
    print(f"Local x: {x}")

change_x()
#refer to screenshot pss35 in readme.md for result
print(f"Global x after change_x(): {x}")

#modify global variable inside a function
def modify_global_x():
    global x
    x = 30
    print(f"Modified global x: {x}")

modify_global_x()
#refer to screenshot pss36 in readme.md for result
print(f"Global x after modify_global_x(): {x}")

#nested function
def outer_function(x):
    #create a function inside a parent function
    def inner_function():
        print(f"x from outer function: {x}")
    inner_function()

#refer to screenshot pss37 in readme.md for result
outer_function(40)

##Creating and Using Modules
#creating modules
touch math_operations.py
def add(a, b):
      return a + b

def subtract(a, b):
      return a - b

def multiply(a, b):
      return a * b

def divide(a, b):
      if b != 0:
         return a / b
      else:
         return "Error: Division by zero"

PI = 3.14159

#create module to excute the code 
touch use_math_module.py

import math_operations

result_add = math_operations.add(5, 3)
result_subtract = math_operations.subtract(10, 4)
result_multiply = math_operations.multiply(2, 6)
result_divide = math_operations.divide(15, 3)

#refer to screenshot pss38 in readme.md for result
print(f"Addition: {result_add}")
print(f"Subtraction: {result_subtract}")
print(f"Multiplication: {result_multiply}")
print(f"Division: {result_divide}")
print(f"Value of PI: {math_operations.PI}")

##Importing Specific Functions from Modules
#creating new file which i will use for importing the function
touch ~/project/advanced_math.py

#import module and the built in function 
# advanced_math.py

import math

def square_root(x):
      return math.sqrt(x)

def power(base, exponent):
      return math.pow(base, exponent)

def sin(angle):
      return math.sin(math.radians(angle))

def cos(angle):
      return math.cos(math.radians(angle))

#create a file to execute the function
touch ~/project/use_advanced_math.py

# use_advanced_math.py
# i use aliases for sin and cos by giving it another variable name.by using aliases 
it makes my code more readable and avoid naming conflicts between different modules.

from advanced_math import square_root, power
from advanced_math import sin as sine, cos as cosine

x = 16
y = 2
angle = 30

print(f"Square root of {x}: {square_root(x)}")
print(f"{x} to the power of {y}: {power(x, y)}")
print(f"Sine of {angle} degrees: {sine(angle)}")
print(f"Cosine of {angle} degrees: {cosine(angle)}")

#running the function
#refer to screenshot pss39 in readme.md for result
python ~/project/use_advanced_math.py

##creating a package, this is a way to organize related modules into a directory hierarchy.
#create a new directory
mkdir ~/project/geometry

#create files inside the directory
touch ~/project/geometry/__init__.py
touch ~/project/geometry/shapes.py

#import module and create function in shapes.py
# geometry/shapes.py

import math

def circle_area(radius):
      return math.pi * radius ** 2

def rectangle_area(length, width):
      return length * width

def triangle_area(base, height):
      return 0.5 * base * height

#create a file to execute the new function
touch ~/project/use_geometry_package.py
# use_geometry_package.py

from geometry.shapes import circle_area, rectangle_area, triangle_area

radius = 5
length = 4
width = 6
base = 3
height = 8

print(f"Area of circle with radius {radius}: {circle_area(radius):.2f}")
print(f"Area of rectangle with length {length} and width {width}: {rectangle_area(length, width)}")
print(f"Area of triangle with base {base} and height {height}: {triangle_area(base, height)}")

#excute the function
#refer to screenshot pss40 in readme.md for result
python ~/project/use_geometry_package.py

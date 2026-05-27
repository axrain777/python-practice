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

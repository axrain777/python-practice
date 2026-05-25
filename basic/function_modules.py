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


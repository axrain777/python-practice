#exploring integer variable
books = 5
#refer to screenshot pss1 in readme.md for result
print(f"I have {books} books.")

#exploring float variable
price = 19.99
#refer to screenshot pss2 in readme.md for result
print(f"This book costs ${price}.")

#calculation using integer and float variable, we use .2f because its a faster way to format the numbers to two decimal places
quantity = 3
total_cost = price * quantity
#refer to screenshot pss3 in readme.md for result
print(f"The total cost for {quantity} books is ${total_cost:.2f}.")

#exploring string variable
name = "Alice"
#refer to screenshot pss4 in readme.md for result
print(f"Hello, {name}!")

#combining two string variables
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
#refer to screenshot pss5 in readme.md for result
print(full_name)

#repeating a string
cheer = "Go! " * 3
#refer to screenshot pss6 in readme.md for result
print(cheer)

# Finding the length of a string
#refer to screenshot pss7 in readme.md for result
print(len(full_name))

# Accessing individual characters
#refer to screenshot pss8 in readme.md for result
print(full_name[0])  # Get the first character
print(full_name[-1]) # Get the last character

#create new string from existing one because strings in python is immutable but we can use this way to modify.
message = "Hello World"
uppercase_message = message.upper()
#refer to screenshot pss9 in readme.md for result
print(uppercase_message)

#exploring boolean
is_learning = True
is_finished = False
#refer to screenshot pss10 in readme.md for result
print(f"Are we learning Python? {is_learning}")

#boolean in comparison operators
x = 5
y = 10
#refer to screenshot pss11 in readme.md for result
print(x < y)   # Is x less than y?
print(x == y)  # Is x equal to y?
print(x != y)  # Is x not equal to y?

#exploring Boolean operators (and, or, not)
a = True
b = False
#refer to screenshot pss12 in readme.md for result
print(a and b)  # True only if both a AND b are True
print(a or b)   # True if either a OR b (or both) are True
print(not a)    # The opposite of a

#Converting Between Data Types because sometimes we need to convert the data type to get the result we want
age_string = "25"
age_number = int(age_string) # Convert string to integer
#refer to screenshot pss13 in readme.md for result
print(age_number + 5)

#convert number to string
count = 50
count_string = str(count)
#refer to screenshot pss14 in readme.md for result
print("The count is " + count_string)

#convert value to boolean,sometimes we want to know if result is true or false based on the input. eg legal age is true if age is above 18
#refer to screenshot pss15 in readme.md for result
print(bool(100))      # Non-zero number
print(bool(0))        # Zero
print(bool("Hello"))  # Non-empty string
print(bool(""))       # Empty string

#simple project to combine everything we learnt above.
#create file user_info.py into project directory
touch ~/project/user_info.py 

# Get user input (input is always a string)
name = input("Enter your name: ")
age_str = input("Enter your age: ")

# Convert age to an integer
age = int(age_str)

# Perform a simple calculation
years_to_100 = 100 - age
is_adult = age >= 18

# Create an output message using an f-string
output = f"""
--- User Information ---
Hello, {name}!
You are {age} years old.
You will be 100 years old in {years_to_100} years.
Are you an adult? {is_adult}
--- End of Report ---
"""

# Print the final result, refer to screenshot pss16 in readme.md for result
print(output)

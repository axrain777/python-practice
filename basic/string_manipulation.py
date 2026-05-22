##create a script that processes an astronaut's name to create a standardized name tag.

#Create a Python script file
touch name_tag_processor.py

#ask user for his name
full_name = input("What is your full name?")

#convert name into uppercase
uppercase_name = full_name.upper()

#replace any space in the name to underscore
name_with_underscores = uppercase_name.replace(" ", "_")

#refer to screenshot pss18 in readme.md for result
print("Enter astronaut's full name:",full_name)
print("Original name:",full_name)
print(f"Processed name tag: ASTRONAUT_{name_with_underscores}")

##this file will include conditional statements and loops exercises.

#exploring if statement
age = 20
#refer to screenshot pss19 in readme.md for result
if age >= 18:
    print("You are an adult.")

#adding else clause in if statement. result will be either one of the outputs condition i indicated.
age = 15
#refer to screenshot pss20 in readme.md for result
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

#adding elseif clause in if statement. use it if you have multiple conditions and result.
age = 65
#refer to screenshot pss21 in readme.md for result
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

##Exploring "For" Loops
#simple for loop using range.
#refer to screenshot pss22 in readme.md for result
for i in range(5):
    print(i)

##exploring multiple arugments in range(), start, end, and step values.
#generates a sequence of numbers starting from 1, up to (but not including) 10, with a step of 2.
#refer to screenshot pss23 in readme.md for result
for i in range(1, 10, 2):
    print(i)

#for loop in list
fruits = ["apple", "banana", "cherry"]
#each round the fruit variable will take a value from the list fruits starting from first one which is apple.
for fruit in fruits:
    print(f"I like {fruit}")#refer to screenshot pss24 in readme.md for result

#using for loop with strings, each round char variable will take a letter from the word Python and convert in uppercase
#refer to screenshot pss25 in readme.md for result
for char in "Python":
    print(char.upper())

#combine a "for" loop with conditional statements. % is a modulo operator,returns the remainder or signed remainder of a division. eg 10 % 2 is 0 because 2 goes into 10 5 times with 0 remainder left. 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#refer to screenshot pss26 in readme.md for result
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

##Exploring While Loop
#simple while loop,repeat code as long as condition is true
count = 0
#refer to screenshot pss27 in readme.md for result
while count < 5:
    print(count)
    count += 1

#a simple game to use while loop because while loop is usually used when we dont know in advance how many times we need to iterate.
#import random toolbox
import random

set number to a random number from 1-10
number = random.randint(1, 10)
guess = 0
#refer to screenshot pss28 in readme.md for result
while guess != number:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number {number}!")

##Nested Loops and Loop Control Statements
#Nested Loops,nested loop is like the hands of a clock: the outer loop is like the hour hand, and the inner loop is like the minute hand.
#Nested Loops is useful and navigating between two dimensioal datas.
for i in range(3):
    for j in range(2):
        #refer to screenshot pss29 in readme.md for result
        print(f"i: {i}, j: {j}")

#creating a simple number analyser
touch ~/project/number_analyzer.py

#create a function so that we can reuse it by prompting the function instead of typing the old code again and again.
#refer to screenshot pss30 in readme.md for result
def analyze_numbers():
    numbers = []
    #creates an "infinite loop" that keeps asking the user for numbers until they explicitly tell it to stop
    while True:
    #This checks if the user typed "done". If they did, break terminates the loop so the program can move to the analysis phase
        user_input = input("Enter a number (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
    #safety logic to prompt warning message instead of crashing the program.   
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")
    #Before moving to next step,checks if the list is empty and exit function  if its empty
    if not numbers:
        print("No numbers entered.")
        return

    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    print(f"\nAnalysis of {len(numbers)} numbers:")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")

    print("\nNumber distribution:")
    for num in numbers:
        if num < average:
            print(f"{num} is below average")
        elif num > average:
            print(f"{num} is above average")
        else:
            print(f"{num} is equal to average")

if __name__ == "__main__":
    analyze_numbers()

#Create a Rocket Launch Countdown program
# Use a for loop with range to create the countdown,range(start,end(not included),step)
for i in range(10, -1, -1):
    print(i)

# After the loop completes, print "Liftoff!"
#refer to screenshot pss31 in readme.md for result
print("Liftoff!")


# Author: Tega Omarejedje
# Assignment: Exploring Python Concepts
# Date: 05/22/2025

# Task 1 - Variables: Your First Python Intro
name = "Tega Omarejedje"
age = 25
height = 5.6
print("Hey there, my name is %s! I'm %d years old and %f feet tall."%(name, age, height))

# Task 2 - Operators: Playing with Numbers
# Perform Addition, Subtraction, Multiplication, Division
num1 = 10
num2 = 3
# 13 will be printed out, which is the addition operator at work. 
print("The sum of 10 and 3 is", num1 + num2)
# 7 will be printed out, which is the subtraction operator at work. 
print("The subtraction of 10 and 3 is", num1 - num2)
# 30 will be printed out, which is the multiplication operator at work. 
print("The multiplication of 10 and 3 is", num1 * num2)
# 3.3333333333333335 will be printed out, which is the division operator at work. 
print("The division of 10 and 3 is", num1 / num2)

# Task 3 - Conditional Statements: The Number Checker
number = int(input("Enter an integer: "))
if number > 0:
    print("This number is positive. Awesome!")
elif number < 0:
    print("This number is negative. Better luck next time!")
else:
    print("Zero it is. A perfect balance!")

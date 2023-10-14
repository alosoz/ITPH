# Question_1 : Write a program to use the same function two times.

# Create a function named print_numbers().
# Inside the function, put two print statements: print(5) and print(100).
# Call the print_numbers() function two times.

def print_numbers():
    print(5)
    print(100)
print_numbers()

# ------------------------------------------------------------------------------------------------------------------------------------

# Question_2 : Write a program to check if the student passed or failed his/her examination by creating a function.

# Create a function named checkMarks() with argument marks.
# Inside the function, check if the user input mark is greater than 70.
# If it is greater than or equal to 70, print Pass. Otherwise, print Fail.Outside the function, take user
# input for marks.
# Call the function using the function name.
# Example Input = 90, Expected output Pass

def checkMarks(marks):
    if marks >= 70:
        print("Pass")
    else:
        print("Faild")

marks = input("enter the mark of the student")
checkMarks(marks)

# ------------------------------------------------------------------------------------------------------------------------------------

# Question_3 : Write a program to check if the two arguments passed are equal or not by creating a function.

# Get two integer inputs num1 and num2.
# Create a function my_function() that accepts two arguments.
# Inside the function, check to see if the two arguments are equal.
# If they are equal, return True, else return False.
# Call the function, pass integers num1 and num2 as arguments to the function, and print the
# returned value.
# Example Input = 1 2, Expected output False

num1 = input("enter the first number")
num2 = input("enter the second number")
def my_function(num1 , num2):
    if num1 == num2:
        return True
    else:
        return False
    
print(my_function(num1,num2))

# ------------------------------------------------------------------------------------------------------------------------------------

# Question_4 : Write a program to print full name with space in between using a function.

# Define a function named full_name() with two arguments first_name and last_name.
# Inside the function, print first_name and last_name and separate them by an empty space.
# Outside the function, take string input for first name and last name and assign them to first and last
# variables.
# Call the function and pass first and last as arguments.


def full_name(first_name,last_name):
    print(first_name, " ", last_name)

first = input("enter the first name")
last = input("enter the last name")

full_name(first,last)

# ------------------------------------------------------------------------------------------------------------------------------------

# Question_5 : Write a program to check whether a number is prime or not using a function.

# A prime number is a number that is only divided by either 1 or itself. For example, 7, 5, 19, etc.
# Define a function named check_prime().
# Inside the function, create a variable named num
# if num is prime number, print Prime Number. Otherwise, print Not Prime Number.
# Outside the function, get an integer input for the number variable.
# Call the function and pass number as an argument.


def check_prime(num):
    if num == 1:
        print("Not Prime Number")
    elif num > 1:
        for i in range(2,num):
            if num % i == 0:
                flag = True
                break
        if flag:
            print("Not Prime Number")
        else:
            print("Prime Number")
    

number = int(input("enter the number"))

check_prime(number)

# ------------------------------------------------------------------------------------------------------------------------------------


# Intermediate


# Question_6 : Write a program to calculate the power of an integer using a function.

# Get an input integer num.
# Create a function calculate_pow with a parameter arg1.
# Return the result of arg1 raised to the power 3.
# Call the function, pass num as its argument, and print the returned value

num = int(input("enter a number"))
def calculate_pow(arg1):
    result = arg1 ** 3
    return result
print(calculate_pow(num))

# ------------------------------------------------------------------------------------------------------------------------------------

# Question_7 : Write a program to print a person's information.

# Create a function named display_info().
# This function must accept two arguments: name and location.
# Print name and location in two separate lines.
# 2. Step 2
# Outside of the function:
# Get string input from the user and assign it to the country variable.
# Call the display_info() with arguments: the "Magnus" string and the country variable, respectively.


def display_info(name, location):
    print(name)
    print(location)

country = input("enter")
display_info("Magnus", country)

# ------------------------------------------------------------------------------------------------------------------------------------

# Question_8 : Write a program to find the sum of N natural numbers by creating a function.

# Define a function named find_sum() that takes n as an argument.
# Inside the function, compute the sum of numbers from 1 to n and return the total.
# Outside the function, get an integer input for a variable number.
# Call the function and pass number as an argument and print the return value


def find_sum(n):
    x = 0
    for i in range(1,n+1):
        x = i + x
    return x
num = int(input("enter the number"))
print("result = ",find_sum(num))

# ------------------------------------------------------------------------------------------------------------------------------------

# Question_9 : Write a program to compute the area of a circle using a function.

# Here's the formula to compute the area of a circle.
# Area = 3.14 * radius * radius
# Create the compute_area() function that accepts float parameters radius and pi.
# Inside the function, compute the area of the circle and return it.
# Outside the function, get a float input value for the radius of the circle.
# Create a float variable named pi with value 3.14.
# Call compute_area() with arguments radius and pi.
# Print the returned value.

def computer_area(radius, pi):
    Area = pi * radius * radius
    return Area
radius_c = float(input("enter the radius"))
pi = 3.14

print("Area of the circle: ", computer_area(radius_c, pi))

# ------------------------------------------------------------------------------------------------------------------------------------


# Advanced


# Question_10 : Create a function named call_me() that takes two arguments a and b.

# Give default value 5 to argument a and 10 to argument b.
# Inside the function, print a and b in two separate lines.
# Outside of the function

# Take integer input and assign it to variable n.
# Call the call_me() function with n as an argument.

def call_me(a = 5, b = 10):
    print(a)
    print(b)

n = int(input("enter an integer"))
call_me(n)

# ------------------------------------------------------------------------------------------------------------------------------------

# Question_11 : Create a function named print_items() that can take any number of arguments.

# Inside the function, use a for loop to print all the arguments passed during the function call
# Outside the function take two string inputs and store them in variables text1 and text2 respectively
# call the print_item() function with text1 as an argument
# call the print_item() function with text1 and text2 as arguments

def print_items(*args):
    for item in args:
        print(item)

text1 = input("enter string1")
text2 = input("enter string2")

print_items(text1)
print_items(text1, text2)
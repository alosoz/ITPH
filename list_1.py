# Question_1 : Write a program to print individual items of a list.

# Create a list named fruits with items "apple", "kiwi", "grapes", "mango".
# Use a for loop to iterate through fruits and print its items.

fruits = ["apple","kiwi","grapes","mango"]

for item in fruits:
    print(item)

# ------------------------------------------------------------------------------------------------------------------------------------

# Question_2 : Write a program to add an item (entered by the user) to the end of the list.

# Create a list named odd_numbers with items 1, 3, and 5.
# Take an integer as input and assign it to number variable.
# Use the append() function to add user input item to the end of the list.
# Print the updated list

odd_numbers = [1,3,5]
number = int(input("enter a number"))

odd_numbers.append(number)
print(odd_numbers)

# ------------------------------------------------------------------------------------------------------------------------------------

# Question_3 : Write a program to calculate the product of list items.

# Create a list my_list and assign [2, 5, 3, 4, 1] to it.
# Declare a variable product with value 1.
# Iterate over my_list and multiply each item to product.
# Print product.

my_list = [2,5,3,4,1]
product = 1

for i in my_list:
    product *= i

print(product)

# ------------------------------------------------------------------------------------------------------------------------------------

# Question_4 : Write a program to check if the first and last characters of a string are equal.

# Take string as input and assign it to check variable.
# Use list indexing to check if the first and the last character of a string are equal or not. use( list() to convert
# a string to list)
# If yes, print Equal. Else print Not Equal.

check = input("enter a string")
list1 = list(check)

if list1[0] == list1[-1]:
    print("Equal")
else:
    print("Not")

# ------------------------------------------------------------------------------------------------------------------------------------

# Question_5 : Write a program to print odd integers from a numbers list.

# Create a list named numbers with integers 1, 2, 3, 4, 5, 6, 7, 8.
# Use a for loop to iterate through numbers.
# Inside the loop, print only odd integers.

numbers = [1,2,3,4,5,6,7,8]
for i in number:
    if i % 2 != 0:
        print(i)

# ------------------------------------------------------------------------------------------------------------------------------------

# Question_6 : Write a program to reverse a given list.

# Create a list my_list and assign [1, 2, 3, 4] to it.
# Create a new list with items in the reverse order and print it.

my_list = [1,2,3,4]
my_list.reverse()
print(my_list)

# ---------2.way---------

my_list = [1,2,3,4]
reversed_list = my_list[::-1]
print(reversed_list)

# ------------------------------------------------------------------------------------------------------------------------------------

# Question_7 :Write a program to create a new list from an existing list using list slicing.

# Create a list named my_list with items 'p','y','t','h','o','n'.
# Use the slicing notation to get a new list from the second to the second-last items from my_list.
# Print the new list.

my_list = ['p','y','t','h','o','n']
new_list = my_list[1:-1]

# ------------------------------------------------------------------------------------------------------------------------------------

# Question_8 : Given a list of numbers, find the sums of even numbers and odd numbers.

# Print both sums in a tuple as (odd_sum, even_sum).
# Assumption: We will assume the list contains only numbers.
# Example Test Input:51 75 69 36 75 44 82 36 Expected Output:```(270, 198)

num_list = [51, 75, 69, 36, 75, 44, 82, 36]

odd_sum = 0
even_sum = 0
for i in num_list:
    if i % 2 == 0:
        odd_sum += i
    else:
        even_sum += i

sum = (odd_sum, even_sum)
print(sum)

# ------------------------------------------------------------------------------------------------------------------------------------

# Question_9 : Given a list of numbers that are already in ascending order, square the numbers.

# But the result should be in ascending order as well
# Assumption: The input numbers are always in ascending order.
# Example Test Input -7 -2 0 4 5, 7Expected Output [0, 4, 16, 25, 49]

num_list = [-7, -2, 0, 4, 5]
num_list.sort()
result_list = []
for i in num_list:
    i *= i
    result_list.append(i)
result_list.sort()
print(result_list)

# ------------------------------------------------------------------------------------------------------------------------------------

# Question_10 : Given a list of numbers, find if the list elements are in ascending sequence or not a sequence at all. 

# Write a Python program that prints,
# True - if the list elements are a perfect sequence
# False - if the list elements are not a sequence
# Example Test Input 1 2 3 4 5 Expected Output True

list1 = [1,2,3,4,5]
for i,j in (list1, list1[1:]):
    if i < list1:
        print(True)
    else:
        print(False)

#yapamadim tekrar bak


# ------------------------------------------------------------------------------------------------------------------------------------


# Advanced


# Question_11 : Create a program to print the occurrence of a character in the string.

# Take string input and store it in the string1 variable.
# Take a character input (a string with a single character) and store it in character1 variable.
# Create a variable named count and initialize it to 0.
# Use a for loop to iterate through string1.
# Inside the loop, check the occurrence of the character in the string. If it's True, increment count by 1.
# Print the count variable

str1 = input("enter a string")
character1 = input("enter a character")
count = 0
for i in str1:
    if i == character1:
        count += 1
print(count)

# ------------------------------------------------------------------------------------------------------------------------------------

# Question_12 : Write a program to replace 'yt' in 'Python' with the string entered by the user.

# Create a string named language with the value "Python".
# Take string as an input for ch variable.
# Use the replace() method to replace "yt" with user-entered string stored in ch.
# Print the new string.
# Hint: Use the string replace() method. This method takes two arguments.
# oldValue - a substring we want to replace
# newValue - a substring that replaces the oldValue
# Example Test Input ab Expected Output Pabhon

language = "Python"
ch = input("enter a string: ")
new_str = language.replace("yt", ch)
print(new_str)

# ------------------------------------------------------------------------------------------------------------------------------------

# Question_13 : Write a program to concatenate two strings.

# Get two string inputs for variables string1 and string2.
# Concatenate these strings and store them in the result variable.
# Print the value of result.

str1 = input("enter first string: ")
str2 = input("enter second string: ")
result = str1 + str2
print(result)

# ------------------------------------------------------------------------------------------------------------------------------------

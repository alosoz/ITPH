# Practicing lists
# We now know of two ways to work with lists: removing an item from it based on the index, and concatenating a value onto an existing list. Let's practise a bit!

# Task 1: Create and a simple list
# 1.	Create an empty list called my_list.
# 2.	Add these items to my_list: 10, 20, 30, 40, 50.
# 3.	Print the contents of my_list.

my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)
print(my_list)

# ------------------------------------------------------------------------------------------------------------------------------------

# Task 2: Access and change list items
# 1.	Save the third item of my_list in a variable called 'item3'
# 2.	Print the value of 'item3'.
# 3.	Change the second item of my_list to 25.
# 4.	Print the updated content of my_list.

item3 = my_list[2]

print(item3)

my_list[1] = 25

print(my_list)

# ------------------------------------------------------------------------------------------------------------------------------------

# Task 3: List Slicing
# 1.	Create a new list called numbers containing the numbers from 1 to 10.
# 2.	Use slicing to create a new list called even_numbers, which contains only the even numbers from numbers. Use the modulo % function for this.
# 3.	Print the even_numbers list.

numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = []
for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)

#2. way:

numbers = list(range(1,11))
even_numbers = [number for number in numbers if number % 2 == 0]

# ------------------------------------------------------------------------------------------------------------------------------------

# Task 4: List Concatenation
# ⦁	Create a list called first_names containing three names: "John", "Joe", and "Jane."
# ⦁	Create a list called last_names containing three last names: "Smith", "Smithson", and "Smithereens."
# ⦁	Concatenate first_names and last_names and save the new list this creates as full_names.
# ⦁	Print the full_names list.

first_name = ["John", "Joe", "Jane"]
last_name = ["Smith", "Smithson", "Smithereens"]
full_names = first_name + last_name
print(full_names) 

#yapamadim

# ------------------------------------------------------------------------------------------------------------------------------------

# Task 5: List Comprehensions
# ⦁	Create a new list called squares that contains the squares of the numbers from 1 to 10, using list comprehension.
# ⦁	Print the squares list.

squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)

# ------------------------------------------------------------------------------------------------------------------------------------


# Task 6: List Methods
# ⦁	Use the index() method to find the index of the element 30 in my_list and store it in a variable called index_30.
# ⦁	Print the value of index_30.
# ⦁	Use the count() method to find the number of occurrences of 50 in my_list and store it in a variable called count_50.
# ⦁	Print the value of count_50.

# ------------------------------------------------------------------------------------------------------------------------------------


# Task 7: List Sorting
# ⦁	Create a list called unsorted_numbers with the following values: 5, 2, 8, 1, 3.
# ⦁	Use the sort() method to sort the elements in unsorted_numbers in ascending order.
# ⦁	Print the sorted list.

# ------------------------------------------------------------------------------------------------------------------------------------


# Bonus Task: List Reversal
# ⦁	Create a list called reverse_me containing five elements in any order.
# ⦁	Reverse the elements of the reverse_me list in-place (i.e., without creating a new list).
# ⦁	Print the reversed reverse_me list.

# Python dictionaries questions 

# Here are some questions/puzzles about Python dictionaries. Take some time to try out the code and get to an answer. 

# Question_1 : What are correct ways to get the value of marks key?

student = {
  "name": "Emma",
  "class": 9,
  "marks": 75
}

m = student.get(2)
m = student.get('marks')
m = student[2])
m = student['marks'])

# answer:
m = student.get("marks")



# ------------------------------------------------------------------------------------------------------------------------------------
# Question_2 : Dictionary keys must be immutable

True  
False

# answer:
True



# ------------------------------------------------------------------------------------------------------------------------------------
# Question_3 : What is the output of the following dictionary operation?

dict1 = {"name": "Mike", "salary": 8000}
temp = dict1.get("age")
print(temp)

KeyError: ‘age’
None

# answer:
None





# ------------------------------------------------------------------------------------------------------------------------------------
# Question_4 :Items are accessed by their position in a dictionary and All the keys in a dictionary must be of the same type.

True
False

#answer:
False


# ------------------------------------------------------------------------------------------------------------------------------------
# Question_5 :Select all correct ways to copy a dictionary in Python

dict2 = dict1.copy()
dict2 = dict(dict1)
dict2 = dict1

#answer:
dict2 = dict1.copy()
dict2 = dict(dict1)


# ------------------------------------------------------------------------------------------------------------------------------------
# Question_6 : Select all correct ways to empty the following dictionary

student = { 
  "name": "Emma", 
  "class": 9, 
  "marks": 75 
}

del student
del student[0:2]
student.clear()

#answer:
student.clear()




# ------------------------------------------------------------------------------------------------------------------------------------
# Question_7 : What is the output of the following code?

sampleDict = dict([
    ('first', 1),
    ('second', 2),
    ('third', 3)
])
print(sampleDict)

[ (‘first’, 100), (‘second’, 200), (‘third’, 300) ]
Options: SyntaxError: invalid syntax
{‘first’: 1, ‘second’: 2, ‘third’: 3}

#answer:
{‘first’: 1, ‘second’: 2, ‘third’: 3}




# ------------------------------------------------------------------------------------------------------------------------------------
# Question_8 : Select the correct way to access the value of a history subject

sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

sampleDict['class']['student']['marks']['history']
sampleDict['class']['student']['marks'][1]
sampleDict['class'][0]['marks']['history']


#answer:
sampleDict['class']['student']['marks']['history']


# ------------------------------------------------------------------------------------------------------------------------------------
# Question_9 : Select the correct way to print Emma’s age.

student = {1: {'name': 'Emma', 'age': '27', 'sex': 'Female'},
           2: {'name': 'Mike', 'age': '22', 'sex': 'Male'}}

student[0][1]
student[1]["age"]
student[0]["age"]


#answer:
student[1]["age"]

# ------------------------------------------------------------------------------------------------------------------------------------
# Question_10 : What is the output of the following dictionary operation

dict1 = {"name": "Mike", "salary": 8000}
temp = dict1.pop("age")
print(temp)

KeyError: ‘age’
# None

#answer:
KeyError: ‘age’


# ------------------------------------------------------------------------------------------------------------------------------------
# Question_11 : What is the output of the following code

dict1 = {"key1":1, "key2":2}
dict2 = {"key2":2, "key1":1}
print(dict1 == dict2)

True
False


#answer:
True


# ------------------------------------------------------------------------------------------------------------------------------------
# Question_12 : Select all correct ways to create an empty dictionary 

sampleDict = {} 

sampleDict = dict() 

sampleDict = dict{} 

sample.cleat 

Other: 


#answer:
sampleDict = {} 

sampleDict = dict() 

Other: empty_dict = {key: value for key, value in []}


# ------------------------------------------------------------------------------------------------------------------------------------

# Create a program that stores names of employees in a dictionary, as well as their age and starting year.

# Let the user choose what they want to do: add info, show info, change info and delete info. 

# You can use 'simple' print- and input-functions to create a menu.

# Extra challenge: store the data in an external file or database.

import json

data_file = "emloyee_data.json"


employee_data = {}



def add():
    name = input("Enter employee name")
    age = input("Enter employee age")
    start_year = input("Enter employee starting year")
    employee_data[name] = {"Age":age,"StartYear":start_year}
    save_data()

def show():
    # name = input("Enter employee name")
    # if name in employee_data:
    #     info = employee_data[name]
    #     print("Name: {}, Age: {}, Starting Year: {}".format(name,info["Age"],info["StartYear"]))
    
    print(employee_data )

def change():
    name = input("Enter employee name")
    if name in employee_data:
        age = input("Enter new age:")
        start_year = input("Enter new starting year")
        employee_data[name]['Age'] = age
        employee_data[name]["StartYear"] = start_year 
        save_data()
    else:
        print("{} not found in the database".format(name))

def delete():
    name = input("Enter employee name")
    if name in employee_data:
        del employee_data[name]
        save_data()
    else:
        print("{} not found in the database".format(name))

    

def save_data():
    with open(data_file, 'w') as file:
        json.dump(employee_data, file)



while True:
    choise = input("""
1. Add employee
2. Show employee
3. Change employee                  
4. Delete employee
5. Exit                   

""")
    if choise == '1':
        add()
    elif choise == '2':
        show()
    elif choise == '3':
        change()
    elif choise == '4':
        delete()
    elif choise == '5':
        break
    else:
        print("Invalid choice. Please enter a valid option from menu")
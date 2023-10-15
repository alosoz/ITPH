import json

# Define the data file to store employee information
data_file = 'employee_data.json'

# Load existing data from the file or initialize an empty dictionary
try:
    with open(data_file, 'r') as file:
        employee_data = json.load(file)
except FileNotFoundError:
    employee_data = {}

# Function to display the menu
def display_menu():
    print("Employee Information Management System")
    print("1. Add Employee Information")
    print("2. Show Employee Information")
    print("3. Change Employee Information")
    print("4. Delete Employee Information")
    print("5. Exit")

# Function to add employee information
def add_employee():
    name = input("Enter employee name: ")
    age = input("Enter employee age: ")
    start_year = input("Enter employee starting year: ")
    employee_data[name] = {'Age': age, 'StartingYear': start_year}
    save_data()

# Function to show employee information
def show_employee():
    name = input("Enter employee name: ")
    if name in employee_data:
        info = employee_data[name]
        print(f"Name: {name}, Age: {info['Age']}, Starting Year: {info['StartingYear']}")
    else:
        print(f"{name} not found in the database.")

# Function to change employee information
def change_employee():
    name = input("Enter employee name: ")
    if name in employee_data:
        age = input("Enter new age: ")
        start_year = input("Enter new starting year: ")
        employee_data[name]['Age'] = age
        employee_data[name]['StartingYear'] = start_year
        save_data()
    else:
        print(f"{name} not found in the database.")

# Function to delete employee information
def delete_employee():
    name = input("Enter employee name to delete: ")
    if name in employee_data:
        del employee_data[name]
        save_data()
    else:
        print(f"{name} not found in the database.")

# Function to save data to the external file
def save_data():
    with open(data_file, 'w') as file:
        json.dump(employee_data, file)

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        show_employee()
    elif choice == '3':
        change_employee()
    elif choice == '4':
        delete_employee()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4/5).")


picnicitems = {'sandwiches':4,'appeels':12,'cups':4,'cookies':8000}



def print_dic():
    title1 = "PICNIC ITEMS"
    print(title1.center(20,'-'))
    
    for key in picnicitems:
        longest_key = len(max(picnicitems, key=len))
        str1 = key
        print(str1.ljust(longest_key+2, '-'),str(picnicitems[key]).rjust(5,))

        
def add():
    item = input("enrer a item")
    count = input("enter the amount")

    picnicitems.update({item:count})

    print(f" {item} has added the list of picinic")

def change():
    item = input("Write the item you want to change")
    count = input("enter the amount")

    picnicitems.update({item:count})

    print(f" {item} has updated")


def delete():
    print_dic()
    del_item = input("chouse the item that you want to delete")
    del picnicitems[del_item]
    print(f" {del_item} has been deleted")


def main():
    while True:
        choise = input("""
    1. Add
    2. Show
    3. Change                  
    4. Delete
    5. Exit                   

    """)
        if choise == '1':
            add()
        elif choise == '2':
            print_dic()
        elif choise == '3':
            change()
        elif choise == '4':
            delete()
        elif choise == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option from menu")



main()
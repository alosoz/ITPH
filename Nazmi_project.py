employees = {'Daniel Ricciardo':(34,2011),'Charles Leclerc':(25,2018),'Lando Norris':(23,2019)} #creating a new dictionary with instances

                                       
while True:
    inp = str(input("Type 'show', 'add' or 'delete':")).lower().strip() #getting input from user as lowercase and getting rid of extra spaces   
    filtered_inp = filter(str.isalpha,inp)                              #filtering the input from unnecessary characters
    inp_new = ''.join(filtered_inp)                                     #getting together the whole input 

    # if inp_new != 'show' and inp_new != 'add' and inp_new != 'delete':
    #     print('Type a valid option')
    #     x = input("If you want to continue press 1")
    #     if x == "1":
    #         continue
    #     else:
    #         break
                                            #getting together the whole input 

    else:
        
        if inp_new == 'show':                                               
            for a in employees.keys():
                print('\nName:',a,'\nAge:',employees[a][0],'\nStarting year:',#if user types 'show', showing all dictionary with for loop
                employees[a][1],'\n')

            continue
        if inp_new == 'add':
            while True:
                name = str(input('Please enter a name and surname:')).strip()   #if user types add, asking for a name and adding it in a list
                raw_name = ''.join(name.split())                                #clearing spaces between words
                if raw_name.isalpha() == False:                                 #checking if it is alphabetic 
                    print('You can enter only letters') 
                    continue
                if len(name.split()) < 2:                                       #checking if user enters at least two words
                    print('Please enter both name and surname')
                    continue
                break
            
            while True:
                age = input('Please enter an age:')                     #asking for a age
                if age.isdigit() == False:                              #checking if it is numeric
                    print('You can enter only numbers')                                                              
                    continue
                age = int(age)
                if age < 18 or age > 67:                                #checking if it is between 18 and 67
                    print('Please enter an age between 18 and 67')
                    continue
                break
            
            while True:
                year = input('Please enter a starting year:')               #asking for a starting year
                if year.isdigit() == False:                                 #checking if it is numeric
                    print('You can enter only numbers')
                    continue
                
                year = int(year)
                if year < 1950 or year > 2023:                          #checking if it is between 1950 and 2023
                    print('Please enter a starting year between 1950 and 2023')
                    continue
                break
            employees[' '.join(name.split()).title()] = (age, year)     #adding new pair in the dictionary

        if inp_new == 'delete':
            delname = str(input('Please enter the name you want to delete:'))#if user types delete, getting the user name to delete 
            del employees[delname]
            
        # else:
            
            
    


#if user enters an invalid option, there must be shown a new string for the input
        
        
employees = {'Daniel Ricciardo':(34,2011),'Charles Leclerc':(25,2018),'Lando Norris':(23,2019)} #creating a new dictionary with instances

                                       
while True:
    inp = str(input("Type 'show', 'add' or 'delete':")).lower().strip() #getting input from user as lowercase and getting rid of extra spaces   
    filtered_inp = filter(str.isalpha,inp)                              #filtering the input from unnecessary characters
    inp_new = ''.join(filtered_inp)                                     #getting together the whole input 

    # if inp_new != 'show' and inp_new != 'add' and inp_new != 'delete':
    #     print('Type a valid option')
    #     x = input("If you want to continue press 1")
    #     if x == "1":
    #         continue
    #     else:
    #         break
                                            #getting together the whole input 

    else:
        
        if inp_new == 'show':                                               
            for a in employees.keys():
                print('\nName:',a,'\nAge:',employees[a][0],'\nStarting year:',#if user types 'show', showing all dictionary with for loop
                employees[a][1],'\n')

            continue
        if inp_new == 'add':
            while True:
                name = str(input('Please enter a name and surname:')).strip()   #if user types add, asking for a name and adding it in a list
                raw_name = ''.join(name.split())                                #clearing spaces between words
                if raw_name.isalpha() == False:                                 #checking if it is alphabetic 
                    print('You can enter only letters') 
                    continue
                if len(name.split()) < 2:                                       #checking if user enters at least two words
                    print('Please enter both name and surname')
                    continue
                break
            
            while True:
                age = input('Please enter an age:')                     #asking for a age
                if age.isdigit() == False:                              #checking if it is numeric
                    print('You can enter only numbers')                                                              
                    continue
                age = int(age)
                if age < 18 or age > 67:                                #checking if it is between 18 and 67
                    print('Please enter an age between 18 and 67')
                    continue
                break
            
            while True:
                year = input('Please enter a starting year:')               #asking for a starting year
                if year.isdigit() == False:                                 #checking if it is numeric
                    print('You can enter only numbers')
                    continue
                
                year = int(year)
                if year < 1950 or year > 2023:                          #checking if it is between 1950 and 2023
                    print('Please enter a starting year between 1950 and 2023')
                    continue
                break
            employees[' '.join(name.split()).title()] = (age, year)     #adding new pair in the dictionary

        if inp_new == 'delete':
            delname = str(input('Please enter the name you want to delete:'))#if user types delete, getting the user name to delete 
            del employees[delname]
            
        # else:
            
            
    


#if user enters an invalid option, there must be shown a new string for the input
        
        



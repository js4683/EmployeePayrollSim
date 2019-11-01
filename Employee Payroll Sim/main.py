#Author: Jashanpreet Singh

from Employee import Employee #import the Employee class
from LinkedList import LinkedList #import the Linked List class

EmployeeLinked = LinkedList() #initialize a list
while True: #to ensure a valid input
    print('Welcome to the Employee Payroll Simulator')
    userInp = input('a. Add a New Employee\n' + 'b. Enter Hours Worked\n' + 'c. Display Payroll\n' + 'd. Update Employee Hourly Rate\n' + 'e. Remove Employee from Payroll\n' + 'f. Exit the Program' + '\n')
    userInp = userInp.lower() #to make the program more user-friendly
    if userInp == 'a': #if option a is selected
        newEmp = Employee() #make a new employee object
        userInp1 = input('Enter the ID of the new employee:\n') #ask for the id
        check = True #check to see if the requirements match to create the new node
        if EmployeeLinked.searchId(userInp1)[0] == True: #handles if the id already exists 
            check = False
            print('Employee ID already taken\n')
        else: #handles if new id
            newEmp.setID(userInp1)
        if check == True: #if the first requirement is met
            userInp2 = float(input('Enter the hourly pay for the new employee: \n')) #ask for the hourly pay
            if userInp2 < 6.00:#handles if the pay is less than 6.00 dollars
                print('Hourly Pay cannot be less than $6.00\n')
                check = False
            else:
                newEmp.setPay(userInp2)
        if check == True: #handles if both requirements are met
            EmployeeLinked.append(newEmp)
    elif userInp == 'b' or userInp == 'c' or userInp == 'd' or userInp == 'e': #handles if the input is b,c,d, or e
        #prints the Linked list
        print('Payroll')
        print('-------')
        print(EmployeeLinked)
        #handles if the input is b
        if userInp == 'b':
            for item in EmployeeLinked: #iterate over the list and ask hours worked for each employee
                userInp1 = float(input('Enter hours worked for Employee ' + item.getID() + ': \n'))
                if userInp1 < 0: #handles if hours are negative
                    print('Number of hours worked cannot be negative.')
                else: #handles if hours are positive 
                    item.setHours(userInp1)
                    item.setWage(round((item.getPay() * item.getHours()), 2))
        elif userInp == 'd' or userInp == 'e': #if the input is d or e
            #handles the assignment of the text of the input box
            key = ''
            key = 'whose Hourly Pay you want to update: \n' if userInp == 'd' else 'you want to remove from the payroll:\n'
            userInp1 = input('Enter the ID of the employee ' + key)
            #checks if the id is in the linked list
            EmployeeObj = EmployeeLinked.searchId(userInp1)
            if EmployeeObj[0] == True:
                #if the input is d
                if userInp == 'd':
                    userInp2 = float(input('Enter the Hourly Pay for this employee: \n')) #asks for the hourly pay
                    if userInp2 < 6.00: #handles if the hourly pay entered is less than 6.00 dollars
                        print('Hourly Pay cannot be less than $6.00\n') 
                    else: #handles if the hourly pay is valid
                        EmployeeObj[1].getData().setPay(userInp2)
                        EmployeeObj[1].getData().setWage(round((EmployeeObj[1].getData().getPay() * EmployeeObj[1].getData().getHours()),2))
                #if the input is e
                else:
                    EmployeeLinked.remove(EmployeeObj[1].getData())
                    print('Done!\n')
            #handles if the id entered is not found
            else:
                print('Employee ID not found\n')
    #if the input is f
    elif userInp == 'f':
        print('Program Exited. Good-Bye!')
        break
    #handles if the input is not a,b,c,d,e or f
    else:
        print('Invalid Input\n')
        
        
        
        
        

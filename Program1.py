#***************************************************************
#
#  Developer:         Jason Swann
#
#  Program #:         1 - Arithmetic Expressions
#
#  File Name:         Program1.py
#
#  Course:            COSC 1336 Programming Fundamentals I
#
#  Due Date:          Sep 8, 2020
#
#  Instructor:        Fred Kumi
#
#  Chapter:           Chapter 2:  Input, Processing, and Output
#
#  Description:
#     Calculate an employee's gross pay per pay period based
#       on differing pay frequencies, given annual income.
#
#***************************************************************

#***************************************************************
#
#  Function:     main
# 
#  Description:  The main function of the program
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def main():
    
    developerInfo()
    
    amount = 32500.00
    
    twiceMonth = amount / 24
    biWeekly = amount / 26
    
    print('Annual Salary           = ', format(amount, '.2f'))
    print('When paid twice a month = ', format(twiceMonth, '.2f'))
    print('When paid bi-weekly     = ', format(biWeekly, '.2f'))
    
    # End of the main function 
    
#***************************************************************
#
#  Function:     developerInfo
# 
#  Description:  Prints Programmer's information
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def developerInfo():
    print('Name:     Jason Swann')
    print('Course:   Programming Fundamentals I')
    print('Program:  One')
    print()
    # End of the developerInfo function

# Call the main function
main()

# End of Program 1

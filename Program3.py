#***************************************************************
#
#  Developer:         Jason Swann
#
#  Program #:         3
#
#  File Name:         Program3.py
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          Sep 17, 2020
#
#  Instructor:        Fred Kumi 
#
#  Chapter:           2 - Input, Processing, and Output
#
#  Description:
#     Calculate property tax given actual value and tax rate
#     using an assessed value of 60% of the actual value.
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

    print('This program calculates the property tax on an assessed value of a property.\n')
    
    # Prompt user for input
    actualValue = float(input('Enter the actual value of the property: '))
    taxRate = float(input('Enter the current tax rate: '))
    
    # Calculate assessed value (60% of actual) and property tax
    assessedValue = .6 * actualValue
    propertyTax = assessedValue * taxRate / 100.0
    # Display results
    print('\n')
    print('The Actual Value is   ', format(actualValue, '10.2f'))
    print('The Assessed Value is ', format(assessedValue, '10.2f'))
    print('The Tax Rate is       ', format(taxRate, '10.2f'))
    print('The Property Tax is   ', format(propertyTax, '10.2f'))
    
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
    print('Program:  Three')
    print()
    # End of the developerInfo function

# Call the main function
main()

# End of Program three

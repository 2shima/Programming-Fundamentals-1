#***************************************************************
#
#  Developer:         Jason Swann
#
#  Program #:         2
#
#  File Name:         Program2.py
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          Sep 11, 2020
#
#  Instructor:        Fred Kumi 
#
#  Chapter:           2 - Input, Processing, and Output
#
#  Description:
#   Calculate and display an average of test scores given five inputs
#   from the user.
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

    # Describe program as per programming solution
    print('This program calculates the average of 5 test scores.')

    # Prompt user for score, convert to int, repeat for 5 total tests
    test1 = int(input('Enter the score for test 1: ')) 
    test2 = int(input('Enter the score for test 2: '))
    test3 = int(input('Enter the score for test 3: '))
    test4 = int(input('Enter the score for test 4: '))
    test5 = int(input('Enter the score for test 5: ')) 

    testAverage = (test1 + test2 + test3 + test4 + test5) / 5.0 # Calculate average as float
    print('\nThe average of the 5 scores is ', testAverage) # Display average

    
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
    print('Program:  Two')
    print()
    # End of the developerInfo function

# Call the main function
main()

# End of Program

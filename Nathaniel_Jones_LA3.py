#-------------------------------------------------------------------------------
# LA3.py
# Student Name: Nathaniel Jones
# Version: 
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that 
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Python Programming Third Edition
#-------------------------------------------------------------------------------
# Any notes to grader: For example: fully implemented, added simple prompt to renter loop
#-------------------------------------------------------------------------------
# Code starts below this line 
#----------------------------------------------------------------------------
while True:
    firstName = input("Enter the student's first name: ").strip()
    lastName = input("Enter the student's last name: ").strip()

    testScore = [] #initialize empty list to store scores
    gradeCount = 1 #initialize counter for loop

    while gradeCount < 5:
        test = [] #initializes input list when loop is entered
        test = float(input('Enter the Score on Test {}: '.format(gradeCount)))
        gradeCount += 1
        testScore += [test] #append input onto test score list

        # get total and average
        testTotal = sum(testScore)
        averageScore = testTotal / len(testScore)

        #find letter grade
        if averageScore >= 92.0:
            letterGrade = 'A'
        elif averageScore >= 84.0:
            letterGrade = 'B'
        elif averageScore >= 76.0:
            letterGrade = 'C'
        elif averageScore >= 70.0: 
            letterGrade = 'D'
        else: 
            letterGrade = 'F'
            
        #return values to user
    print('Name: ', firstName, lastName)
    print('Average test score: ', averageScore)
    print('Letter grade: ', letterGrade)
    
    # Ask the user if they want to enter another student
    if input('Would you like to enter another student y/n? ') != 'y':
        break
                     

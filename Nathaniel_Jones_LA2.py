#-------------------------------------------------------------------------------
# LA2.py
# Student Name: Nathaniel Jones
# Version: 1
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that 
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: 
#-------------------------------------------------------------------------------
# Any notes to grader: For example: fully implemented
#-------------------------------------------------------------------------------
# Code starts below this line 
#----------------------------------------------------------------------------
wordCount = 0
while True:
    word = input('Enter a word or type 0 to exit the program: ')
    wordCount +=1
    if word == ('0'):
        wordCount -=1
        break
print('Word count: ', wordCount)
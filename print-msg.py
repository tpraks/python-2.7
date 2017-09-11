#!/usr/bin/python
#Python program to test print statement and comments
'''

Python Program to Test Various Print formats...
-----------------------------------------------

'''
print "\n Python Program to Test Various Print formats... \n -----------------------------------------------\n"
userName='Prakash'
userPlace='Madurai'
userAge=37
userACBalance=12.34567

message = "%s is from %s, and his age is %d and has a account balane of %4.2f" %( userName, userPlace, userAge, userACBalance )

message2 = "{1:s} is the place where {0:s} lives, and he has  {3:4.2f} in his account balane at the age of {2:d}" .format( userName, userPlace, userAge, userACBalance )

print "\n", message
print 
print message2, "\n"

line = "hello how are you\n I am testing the new line escape sequence \n this seems to work"

print line

print " \n-----------------------------------------------\n"

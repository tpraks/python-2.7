#!/usr/bin/python
# Python program to test interactive input and output


# Enter a dict of Name and Age

myNewdict = {}
newName = ""

newName = raw_input("Enter Name:")
newAge = raw_input("Enter Age:")

message = "New Name: %s New Age: %s" %(newName, newAge)
print ( "New Name: %s New Age: %s" %(newName, newAge))
print ( "New Name: {0:s} New Age: {1:d}" .format( newName, int(newAge) ))
print (message)
#myNewdict{newName} = newAge

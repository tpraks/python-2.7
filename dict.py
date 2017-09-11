#!/usr/bin/python

import operator
#Program to test and practice python dictionary
'''
Also try to test tuple and list
Since I have not tried them either

'''

print "This Program is to test Dictionary, List and Tuple in python \n"
print "-------------------------------------------------------------\n"

print "Testing List"

myList=[1,2,3,"Prakash","Babu"]
print (myList)
print myList[0]
print myList[1]
print myList[2]
print myList[3]
print myList[4]
print myList[0] , myList[1], myList[3]+myList[4]

del myList[4]
print "List after deleting element 5"
print myList

myList.append("Babu")
print "List after adding element 5"
print myList

print "Testing Tuple"
print "--------------"


myMonths=("Months", "Jan", "Feb", "Mar", "Apr","May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec")

print myMonths[7]
print myMonths[7+1]

#Testing Slicing

myNewList=myList[1:4]
print "My New List...\n"
print myNewList

print myNewList[4:1]
print myNewList[-3]

#Dictionary is a Key Value Pair

myDictionary={"Prakash":37, "Babu":26, "Ananthi":29}
print "Here is the new dictionary...\n"
print "----------------------------------\n"
print myDictionary

print myDictionary["Prakash"]
myDictionary["Babu"]=39

print myDictionary

# Adding to Dictionary

myDictionary["Thanase"]=65

print myDictionary

del myDictionary["Babu"]
print myDictionary

myDictionary["Sherlyn"]=3
print "--------------------"
print myDictionary
print myDictionary.items()
print myDictionary.keys()
print sorted(myDictionary.items())
print sorted(myDictionary.keys())
print sorted(myDictionary.keys())
print sorted(myDictionary.items(),key=operator.itemgetter(0))
new_dict=sorted(myDictionary.items(),key=operator.itemgetter(1))
b_dict=new_dict
if new_dict==b_dict:
	print "Equal"
else:
	print "Dict unequal"

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    #print ("aStr:" + aStr)
    if aStr == '':
        return False
    if len(aStr) == 1:
		return char == aStr
    
	midChar=len(aStr)/2
	midC=aStr[midChar]
	
	if char == midC:
		# We found the character!
		return True
    elif midC < char:
        #print ("in < " + aStr)
        isIn(char, aStr[midChar+1:])
    else:
        #print ("in > " + aStr)
        isIn(char, aStr[:midChar])


print isIn("a","abcdefg")
print isIn("u","adfghjmpsux")
print isIn("z","abdcefg")
print isIn("z","abdcefgz")

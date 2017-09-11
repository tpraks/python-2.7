def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.    
    '''
    # Your code here
    if a < b:
        a += b
        b = a - b
        a = a - b
   
    if (a%b) == 0 :
        gcd=b   
    else:
         itr=b/2
         gcd=1
         while itr > 0:
            if (a%itr == 0) and (b%itr == 0):
            	gcd=itr
                break
				itr -= 1
    return gcd


a=input()
b=input()
print gcdIter(a, b)

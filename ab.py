a=input()
b=input()
print a, b
if a < b:
	a += b
	b = a - b
	a = a - b
print a, b
if (a/b == 1) and (a%b == 0):
	gcd = b
else:
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
print gcd
	
			 

#!/usr/bin/python -tt
import sys

def Hello(name):
	if name == "prakash" or name == "babu":
		name += '???'
	else:
		DoesNotExist(name)
	print "hello " , name
	print "isn't it", name.upper()
	print "length of name : ", len(name)
	n=len(name)-1
	i=0
	revname[]="\0"
	while n >= 0:
		print name[n]
		revname[i]=name[n]
		n-=1
		i+=1
		

	

def main():
	print "Hello World\n"
	Hello(sys.argv[1])

# boiler plate template

if __name__ == '__main__':
	main()

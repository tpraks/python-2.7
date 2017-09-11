import operator
d={}
with open('t.txt') as f:
	for line in f:
		(key,val,val1)=line.split()
		d[key]=(val,val1)
		e=sorted(d.items(),key=operator.itemgetter(2))


print d
print e
		

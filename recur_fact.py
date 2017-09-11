# 0 1 1 2 3 5 8 13 21 
def recur_fact(x):
	facto=1
	if x == 0:
		return 1
	facto=x * recur_fact(x - 1)
	return facto


x = 5
print recur_fact(x)

def recur_power(base, exp):
	if ( exp < 1 ):
		return base
	else:
		return base * recur_power(base, exp-1)

base=2
exp=4

print recur_power(base,exp)


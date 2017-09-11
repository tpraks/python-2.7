def recur_fibo(n):
	if n < 2:
		return n
	else:
		return recur_fibo(n-1) + recur_fibo(n-2)



n = 5
print recur_fibo(5)

def fibo(n):
  if ( n == 0 or n == 1 ) : 
    return n
  return fibo(n - 2) + fibo(n - 1) 
  

num = input("Enter number of series for fibo:")
for fiboof  in range(num):
  print fibo(fiboof)



def fib(n):
    if n < 0:
        print ("Error: Val less than 0")
        return 0
    if n == 0 or n == 1:
        return n
    else:
#        print fib(n-2) + fib(n-1)
        return fib(n-2) + fib(n-1)


startNumber = int(raw_input("Enter the start number here "))
for fibo_of in range(startNumber):
  print fib(fibo_of)

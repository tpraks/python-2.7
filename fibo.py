startNumber = int(raw_input("Enter the start number here "))

def fib(n):
    if n < 0:
        print ("Error: Val less than 0")
        return -1
    if n == 0 or n == 1:
        return n
    else:
        print fib(n-2) + fib(n-1)
        return fib(n-2) + fib(n-1)


print fib(startNumber-1)

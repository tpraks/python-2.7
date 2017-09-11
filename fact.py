def fact(n):
  if ( n == 1 ): 
    return 1
  else:
    return n * fact( n - 1 )


num = input("Enter number to print its factorial:")
print (fact(num))

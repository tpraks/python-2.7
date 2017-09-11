def num_add(num):
  if  ( num  == 1 ):
    return num
  else:
    return ( num + num_add(num-1) )

num = input("Enter a number to find the sum of all numbers upto it: " )
print ("Sum of Num:")
print ( num_add(num) )
 

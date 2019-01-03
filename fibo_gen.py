def mygen_fibo(n):
  a=0
  b=1
  if i < 0:
    return -1
  for i in range(n):
    yield a
    tmp = a
    a = b
    b += tmp 
#    a, b = b, a+b

for num in mygen_fibo(10):
  print num

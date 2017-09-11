def mygen_fibo(n):
  a=0
  b=1

  for i in range(n):
    yield a
    a, b = b, a+b

for num in mygen_fibo(10):
  print num

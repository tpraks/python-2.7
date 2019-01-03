class fibo_gen:
  def __init__(self):
    self.cache = {}

  def fib(self,n):
    if n < 0:
      raise Exception("Negative Value")

    if n in [0,1]:
      return n

    if n in self.cache:
      return self.cache[n]
     
    fibo = self.fib(n-1) + self.fib(n-2)
    self.cache[n] = fibo

    return fibo


test = fibo_gen()
print test.fib(6-1)

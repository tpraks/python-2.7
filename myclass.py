class Test(object):
  pass

class Newclass(object):
  def __init__(self,myattr):
    self.myattr = myattr

x = Test()
print (x)
y = Newclass(myattr='test')

print y.myattr


import re

def fix_start(s):
  # +++your code here+++
  print s[0]+s[1:].replace(s[0], "*")
  return

def mix_up(a, b):
  #print b[0:2]+a[2:]+" "+a[0:2]+b[2:]
  return b[0:2]+a[2:]+" "+a[0:2]+b[2:]


words=['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
s="abcdabcdabcd"
fix_start(s)
print mix_up("Andy", "Pondy")


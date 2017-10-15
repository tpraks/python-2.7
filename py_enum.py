#Sample Program to test enumerate

def test_enum(array):
  for index, value in enumerate(array):
	print("Index of value: %d is %d" % (value,index))
  

def main():
  test_enum([5,6,7,4,3,2,8,9])


if  __name__ == '__main__':
  main()

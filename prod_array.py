def test_result(arr):
  prod=1
  result_arr = []
  for val in arr:
    prod *= val
  for val in arr:
    result_arr.append(prod/val)
  return result_arr

def main():
  arr = [5,4,6,3,2,8,1]
  prod_arr = []
  pre_prod = 1
  post_prod = 1
  prod_arr.append(1)
  print len(arr)-1
  for i in range(1,len(arr)):
    pre_prod *= arr[i-1]
    prod_arr.append(pre_prod)
  print prod_arr
  for i in range(len(arr)-2,-1,-1):
    post_prod *= arr[i+1]
    prod_arr[i] *= post_prod

  print arr, prod_arr 

  print "Test Result"
  print test_result(arr)

if __name__ == '__main__':
  main()
	

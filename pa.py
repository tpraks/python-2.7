def test_result(arr):
  prod=1
  result_arr = []
  zero=1
  num_zero = 0
  for val in arr:
    if val == 0:
      zero = 0
      num_zero += 1
      continue
    prod *= val
  for val in arr:
    try:
      result_arr.append(prod/val*zero)
    except ZeroDivisionError as err:
      print ('Handling Zero Divsion Error', err)
      if num_zero > 1:
       result_arr.append(prod*0)
      else:
       result_arr.append(prod)
  return result_arr

def main():
  arr = [5,4,6,1,2,8,10]
  prod_arr = []
  pre_prod = 1
  post_prod = 1
  prod_arr.append(1)
  print ("len of array : %d" % (len(arr)))
  for i in range(1,len(arr)):
    pre_prod *= arr[i-1]
    prod_arr.append(pre_prod)
  for i in range(len(arr)-2,-1,-1):
    post_prod *= arr[i+1]
    prod_arr[i] *= post_prod
        
  print arr, prod_arr 

  print "Test Result"
  print test_result(arr)

if __name__ == '__main__':
  main()


# 5,5,20,120,360,720,5760


	

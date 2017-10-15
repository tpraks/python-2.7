
def max_prod_3(list_of_ints):
  max1=list_of_ints[0]
  max2=list_of_ints[1]
  max3=list_of_ints[2]
  for index in range(1,len(list_of_ints)):
    max3 = max(max3,min(list_of_ints[index],max2))
    max2 = max(max2,min(list_of_ints[index],max1))
    max1 = max(max1,list_of_ints[index])
  return max1,max2,max3


def main():
  arr=[100,75,5,6,7,4,3,8,9,10,2,3,21,45,85]
  arr2=[-1,-75,-5,-6,-7,-4,-3,-8,-9,-10,-2,-3,-21,-45,-85]
  print arr
  max1,max2,max3 = max_prod_3(arr)
  print ("max1:%d, max2:%d, max3:%d" % (max1,max2,max3))
  print ("prod_of_max_three: %d" % (max1*max2*max3))
  print arr2
  max1,max2,max3 = max_prod_3(arr2)
  print ("max1:%d, max2:%d, max3:%d" % (max1,max2,max3))
  print ("prod_of_max_three: %d" % (max1*max2*max3))





if __name__ == '__main__':
  main()

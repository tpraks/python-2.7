def max_prod_k(k,list_of_ints):
  max_list = []
  for index in range(k):
    max_list.append(list_of_ints[index])

  for index in range(1,len(list_of_ints)):
    for index_max in range(k-1,-1,-1):
     max_list[index_max] = max(max_list[index_max],min(list_of_ints[index],max_list[index_max-1]))
  return max_list


def main():
  arr=[100,75,5,6,7,4,3,8,9,10,2,3,101,76,21,45,85]
  arr2=[-1,-75,-5,-6,-7,-4,-3,-8,-9,-10,-2,-3,-21,-45,-85]
  print max_prod_k(5,arr)
  print max_prod_k(5,arr2)
  





if __name__ == '__main__':
  main()

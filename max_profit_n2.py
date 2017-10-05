def max_profit(price_list):
  min_index=max_index=0
  n=len(price_list)
  diff = best_diff = 0
  for i in range(n) :
    new_diff = 0
    for j in range(i+1,n):
      if price_list[j] >= price_list[i]:
        diff = price_list[j] - price_list[i]
        if diff > new_diff:
          new_diff = diff
          max_index = j
        else:
          continue
    if best_diff < new_diff:
      best_diff = new_diff
      min_index = i
  return(min_index,max_index,best_diff) 

        

def main():

  stock_price_in_a_day=[]

  # Input test values

  for list in [[5,6,15,3,2,4,7,4,3,1,29,7,8,8,6,35,23,25],[30,6,15,3,2,4,7,4,3,7,20,7,8,8,6,35,23,25],[5,6,15,3,2,4,7,4,3,8,25,7,8,8,6,1,23,20],[5,6,15,3,21,4,7,41,33,20,29,7,8,8,6,5,23,5],[5,6,15,31,32,34,7,4,3,11,29,7,8,8,6,35,23,25],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],[21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]]:
    stock_price_in_a_day.append(list)

  print stock_price_in_a_day
  for stock_price in stock_price_in_a_day:
    print "\n %s" % stock_price
    min_index,max_index,max_prof = max_profit(stock_price)
    print "m_index: %d ma_index: %d ma_profit: %d"  % (min_index, max_index, max_prof)



if __name__ == '__main__':
  main()

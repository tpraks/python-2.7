"""

Problem Description:
===================
Suppose we could access yesterday's stock prices as an array, where:

The indices are the time in minutes past trade opening time, which was 9:30am local time.
The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stockPricesYesterday[60] = 500.

Write an efficient function that takes stockPricesYesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

For example:

  int[] stockPricesYesterday = new int[] {10, 7, 5, 8, 11, 9};

getMaxProfit(stockPricesYesterday);
// returns 6 (buying for $5 and selling for $11)

"""
def min(a,b):
  if a >= b: 
    return b
  else:
    return a

def max(a,b):
  if a >= b:
    return a
  else:
    return b

def max_profit(price_list):
  temp_min_index=min_index=max_index=0
  diff = best_diff = 0
  n=len(price_list)
  i = 1  
  while i < n :
    if price_list[i] <= price_list[temp_min_index]:
      temp_min_index = i
    else:
      diff = price_list[i] - price_list[temp_min_index]
      if (diff >= best_diff):
        best_diff = diff
        min_index = temp_min_index
        max_index = i
      else:
        diff = price_list[i] - price_list[min_index]
        if (diff >= best_diff):
          best_diff = diff
          temp_min_index = min_index
          max_index = i
    i+=1
  return(min_index+1, max_index+1, best_diff)

def get_max_profit_o(stock_prices_yesterday):

  if len(stock_prices_yesterday) < 2:
    raise IndexError('Getting a profit requires at least 2 prices')

  min_price = stock_prices_yesterday[0]
  max_profit_o = stock_prices_yesterday[1] - stock_prices_yesterday[0]

  for index, current_price in enumerate(stock_prices_yesterday):

    if index == 0:
      continue

    potential_profit = current_price - min_price
    max_profit_o = max(max_profit_o, potential_profit)
    min_price  = min(min_price, current_price)

  return max_profit_o

def get_max_profit_on(stock_price_list):
  if len(stock_price_list) < 2:
    raise IndexError('Need atleast 2 values in the list')

  min_price = stock_price_list[0]
  max_profit = stock_price_list[1] - stock_price_list[0]

  for index, current_price in enumerate(stock_price_list):
    if index == 0:
      continue
    profit = current_price - min_price
    max_profit = max(max_profit, profit)
    min_price = min(min_price, current_price)
  return max_profit

def main():

  stock_price_in_a_day=[]

  # Input test values - Different test cases:

  for list in [[5,6,15,3,2,4,7,4,3,1,29,7,8,8,6,35,23,25],[30,6,15,3,2,4,7,4,3,7,20,7,8,8,6,35,23,25],[5,6,15,3,2,4,7,4,3,8,25,7,8,8,6,1,23,20],[5,6,15,3,21,4,7,41,33,20,29,7,8,8,6,5,23,5],[5,6,15,31,32,34,7,4,3,11,29,7,8,8,6,35,23,25],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],[21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]]:
    stock_price_in_a_day.append(list)

  # Call the function for all test inputs above:

  for stock_price in stock_price_in_a_day:
    print "\n %s" % stock_price
    min_index,max_index,max_prof = max_profit(stock_price)
    print "m_index: %d ma_index: %d ma_profit: %d"  % (min_index, max_index, max_prof)
  print "---------------------------------------------"
  for stock_price in stock_price_in_a_day:
    print "\n %s" % stock_price
    print "ma_profit_o: %d"  % get_max_profit_o(stock_price)
  print "--------stock_price_on------------------------------"
  for stock_price in stock_price_in_a_day:
    print "\n %s" % stock_price
    print "ma_profit_o: %d"  % get_max_profit_on(stock_price)


if __name__ == '__main__':
  main()

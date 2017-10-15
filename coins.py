def change_possibilities_bottom_up(amount, denominations):
  ways_of_doing_n_cents = [0] * (amount + 1)
  print "Printing Array after initialization..."
  print ways_of_doing_n_cents
  ways_of_doing_n_cents[0] = 1

  for coin in denominations:
    print("For coin in : %d" % coin)
    for higher_amount in xrange(coin, amount + 1):
      print("For higher_amount in : %d" % higher_amount)
      higher_amount_remainder = higher_amount - coin
      ways_of_doing_n_cents[higher_amount] += ways_of_doing_n_cents[higher_amount_remainder]
      print "+++++++++++++++++ WAY OF DOING N CENTS +++++++++++++++++++"
      print ("way of doing n cents \[higher amount\]: %d is: %d" % (higher_amount,ways_of_doing_n_cents[higher_amount]))
      print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
  return ways_of_doing_n_cents[amount]

def main():

  print ("Number of possibilities for value: %d is: %d" % (124,change_possibilities_bottom_up(124,[1,5,10,25,50,100])))
#  print ("Number of possibilities for value: %d is: %d" % (124,change_possibilities_bottom_up(5,[5,2,1])))

if __name__ == '__main__':
  main()

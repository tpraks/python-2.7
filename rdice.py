from random import randint

def rand7():
  return randint(1,7)


def main():
  dice_roll=7
  while dice_roll > 5:
    dice_roll=randint(1,7)
  print ("dice_roll %d", dice_roll)

if __name__ == '__main__':
    main()
    
  

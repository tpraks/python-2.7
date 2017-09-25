def reverse(str):
  if len(str)==1:
    return str
  else:
    return reverse(str[1::]) + str[0]

def main():
  str1 = raw_input("Enter String: ")
  print str1
  print reverse(str1)


if __name__ == '__main__':
    main()


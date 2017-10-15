def anagram(mystr):
  if len(mystr) == 0:
    return []
  elif len(mystr) == 1:
    return mystr
  else:
    tmp_str = []
    for i in range(len(mystr)):
      substri = mystr[i]
      rest_of_str = mystr[:i] + mystr[i+1:]
      for anagram_substr in anagram(rest_of_str):
        print [substri]
        print anagram_substr
        tmp_str.append([substri]+anagram_substr)
      return tmp_str


if __name__ == '__main__':
  print anagram("abc")

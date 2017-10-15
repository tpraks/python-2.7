def anagrams(word):
    """ Generate all of the anagrams of a word. """ 
    if len(word) < 2:
        yield word
    else:
        for i, letter in enumerate(word):
            print i, letter
            if not letter in word[:i]: #avoid duplicating earlier words
                for j in anagrams(word[:i]+word[i+1:]):
                    print ("Inside J:%s" % j)
                    yield j+letter 

if __name__ == "__main__":
    for i in anagrams("abc"):
        print i

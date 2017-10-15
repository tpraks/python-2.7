def anagrams(word):
    if len(word) < 2:
        return word
    else:
        tmp = []
        for i, letter in enumerate(word):
            for j in anagrams(word[:i]+word[i+1:]):
                tmp.append(j+letter)
    return tmp

if __name__ == "__main__":
    anagram_list =  anagrams("abc")
    print anagram_list

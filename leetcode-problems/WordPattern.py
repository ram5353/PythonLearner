def wordPattern(pattern, s):
    words_list = s.split()
    dict = {}
    if len(words_list) != len(pattern):
        return False
    for i, letter in enumerate(pattern):
        if letter in dict.keys():
            if dict[letter] != words_list[i]:
                return False
        elif words_list[i] in dict.values():
            return False
        else:
            dict[letter] = words_list[i]
    return True


print(wordPattern("abba", "dog dog dog dog"))

# "aaa"
# "aa aa aa aa"
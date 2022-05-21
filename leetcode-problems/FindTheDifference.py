from collections import Counter

#hashmap
def findTheDifference(s, t):
    s_counter = Counter(s)
    for letter in t:
        if letter not in s_counter or s_counter[letter] == 0:
            return letter
        else:
            s_counter[letter] -= 1

#sorting
def findTheDifferenceSorting(s, t):
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    i = 0
    while i < len(t):
        if sorted_s[i] != sorted_t[i]:
            return sorted_t[i]
        i += 1

print(findTheDifference("abba", "abbaa"))

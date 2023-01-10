def isAnagram(s, t):
    first = [x for x in s]
    second = [x for x in t]
    if sorted(first) == sorted(second):
        return True
    return False

# print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
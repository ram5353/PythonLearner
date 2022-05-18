
def lengthOfLongestSubstring(s: str):
    maximum = 0
    list = []
    i = 0
    j = 0
    while j < len(s):
        if s[j] not in list:
            list.append(s[j])
            maximum = max(maximum, len(list))
            j += 1
        else:
            list.remove(s[i])
            i += 1
    print(list)
    return maximum

print(lengthOfLongestSubstring("dvadf"))
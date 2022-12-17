def lengthOfLongestSubstring(s):
    start = 0
    end = 0
    max_length = 1
    result = []
    j = 0
    while j < len(s):
        if s[j] not in result:
            result.append(s[j])
            max_length = max(max_length, len(result))
            j += 1
        else:
            result.pop(0)
    return max_length

print(lengthOfLongestSubstring("bbbbbbbbbbb"))



        

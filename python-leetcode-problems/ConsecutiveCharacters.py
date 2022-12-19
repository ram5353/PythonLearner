def maxPower(s):
    start = 0
    end = 0
    max_length = 1
    count = 0
    if len(s) == 1:
        return 1
    for i in range(0, len(s)-1):
        end += 1
        if s[start] == s[end]:
            count = end - start + 1
            max_length = max(max_length, count)
        else:
            count = 0
            start = end
            
    return max_length

print(maxPower("abbcccddddeeeeedcba"))
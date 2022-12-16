def characterReplacement(s: str, k: int):
    l = 0
    result = 0
    dict = {}
    for r in range(len(s)):
        dict[s[r]] = 1 + dict.get(s[r], 0)
        while (r - l + 1) - max(dict.values()) > k:
            dict[s[l]] -= 1
            l += 1
        result = max(result, r - l + 1)
    return result


print(characterReplacement("AABABBA", 1))
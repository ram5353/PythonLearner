def longestCommonPrefix(strs):
    if not strs: return ""
    longest_prefix = strs[0]
    for i in range(1, len(strs)):
        while(strs[i].find(longest_prefix) != 0):
            longest_prefix = longest_prefix[:-1]
            if len(longest_prefix) == 0:
                return ""
    return longest_prefix

print(longestCommonPrefix(["flower","flow","flight"]))

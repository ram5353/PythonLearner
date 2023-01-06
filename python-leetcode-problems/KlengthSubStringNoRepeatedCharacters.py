from collections import Counter


# def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
#     currSet = []
#     i = 0
#     count = 0
#     for j in range(len(s)):
#         while s[j] in currSet:
#             currSet.remove(s[i])
#             i += 1
#         currSet.append(s[j])
#         if len(currSet) > k:
#             currSet.remove(s[i])
#             i += 1
#         if len(currSet) == k:
#             count += 1
#     return count

def numKLenSubstrNoRepeats(s: str, k: int) -> int:
    if len(s) < k:
        return 0
    count = Counter(s[:k])
    distinct = len(count)
    max_number = 0
    if distinct == k:
        max_number += 1
    for i in range(k, len(s)):
        count[s[i-k]] -= 1
        if count[s[i-k]] <= 0:
            del count[s[i-k]]
        if count[s[i]] == None:
            count[s[i]] = 1
        count[s[i]] += 1
        distinct = len(count)
        if distinct == k:
            max_number += 1
    return max_number

print(numKLenSubstrNoRepeats("havefunonleetcode", 5))


    
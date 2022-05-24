from collections import Counter


def largestUniqueNumber(nums):
    count = Counter(nums)
    maximum = 0
    for c in count:
        if count[c] == 1:
            maximum = max(maximum, c)
    if maximum == 0:
        return -1
    return maximum


print(largestUniqueNumber([5,7,3,9,4,9,8,3,1]))
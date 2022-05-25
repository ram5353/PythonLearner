from collections import Counter


def numIdenticalPairs(nums):
    count = 0
    if len(nums) == len(set(nums)):
        return 0
    for n in range(0, len(nums)):
        for j in range(n + 1, len(nums)):
            if nums[n] == nums[j]:
                count += 1
    return count

def numIdenticalPairsOptimized(nums):
    c = Counter(nums)
    count = 0
    for each in c:
        if c[each] > 1:
            count += sum(range(0, c[each]))
    return count



print(numIdenticalPairsOptimized([1,2,3,1,1,3]))

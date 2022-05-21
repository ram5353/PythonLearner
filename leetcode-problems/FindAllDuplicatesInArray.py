from collections import Counter


def findDuplicates(nums: []):
    result = []
    c = Counter(nums)
    for number in c:
        if c[number] == 2:
            result.append(number)
    return result

def findDuplicatesOptimized(nums):
    result = []
    for num in set(nums):
        if nums.count(num) == 2:
            result.append(num)
    return result

print(findDuplicatesOptimized([4,3,2,7,8,2,3,1]))
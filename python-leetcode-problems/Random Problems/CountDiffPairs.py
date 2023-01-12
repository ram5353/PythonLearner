from collections import Counter


def countKDifference(nums, k):
    counter = Counter(nums)
    result = 0
    for c in counter:
        if k > 0 and c + k in counter:
            result += 1
        elif k == 0 and counter[c] > 1:
            result += 1
    return result   

def countKDifferenceTwoPointer(nums, k):
    nums.sort()
    left = 0
    right = 0
    result = 0
    while left < len(nums) and right < len(nums):
        if left == right or nums[right] - nums[left] < k:
            right += 1
        elif nums[right] - nums[left] > k:
            left += 1
        else:
            left += 1
            result += 1
            while left < len(nums) and nums[left] == nums[left -1]:
                left += 1
    return result
        














print(countKDifferenceOptimized([1,3,1,5,4], 2))
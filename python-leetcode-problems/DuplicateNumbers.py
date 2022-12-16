from collections import Counter


def findDuplicate(nums):
    nums.sort()
    for i in nums:
        if i < len(nums) - 1 and nums[i] == nums[i+1]:
            return nums[i]


    

print(findDuplicate([1,1]))
def twoSum(nums, target):
    dict = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if dict.__contains__(diff):
            return [i, dict.get(diff)]
        dict.__setitem__(nums[i], i)

print(twoSum([2,7,9,11], 9))
        



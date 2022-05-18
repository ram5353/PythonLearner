
def two_sum(nums, target):
    dict = {}
    for i in range(len(nums)):
        difference = target - nums[i]
        if dict.__contains__(difference):
            return [dict.get(difference), i]
        dict.__setitem__(nums[i], i)


print(two_sum([3,2,4], 6))





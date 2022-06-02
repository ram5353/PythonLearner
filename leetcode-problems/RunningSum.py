def runningSum(nums):
    result = [nums[0]]
    for i in range(1, len(nums)):
        result.append(result.__getitem__(i-1) + nums[i])
    return result

print(runningSum([1]))

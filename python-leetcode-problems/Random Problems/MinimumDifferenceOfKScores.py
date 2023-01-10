def minimumDifference(nums, k):
    nums.sort()
    start = 0
    end = k - 1
    result = float("inf")
    while start < len(nums)-k+1:
        result = min(result, nums[end] - nums[start])
        start += 1
        end += 1
    return result

print(minimumDifference([9,4,1,7], 2))




    

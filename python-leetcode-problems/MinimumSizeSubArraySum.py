def minSubArrayLen(target, nums):
    start = 0
    end = 0
    current_sum = 0
    min_length = float('inf')
    while end < len(nums):
        current_sum += nums[end]
        end += 1
        while (start < end and current_sum >= target):
            current_sum -= nums[start]
            start += 1
            min_length = min(min_length, end - start + 1)
    if sum(nums) < target:
        return 0
    return min_length

print(minSubArrayLen(7, [2,3,1,2,4,3]))
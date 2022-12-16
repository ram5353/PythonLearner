def maxOperations(nums, k):
    nums.sort()
    start = 0
    end = len(nums) - 1
    count = 0
    current_sum = 0
    while start < end:
        if nums[start] + nums[end] == k:
            count += 1
            start += 1
            end -= 1
        elif nums[start] + nums[end] < k:
            start += 1
        elif nums[start] + nums[end] > k:
            end -= 1
    return count

print(maxOperations([3,1,3,4,3], 6))


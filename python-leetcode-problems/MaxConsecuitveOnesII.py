def longestOnes(nums, k):
    start = 0
    end = 0
    zeroCount = 0
    max_length = 0
    if all([n == 0 for n in nums]):
            return 0
    for end in range(len(nums)):
        if nums[end] == 0:
            zeroCount += 1
        while start < end and zeroCount > k:
            if nums[start] == 0:
                zeroCount -= 1
            start += 1
        max_length = max(max_length, end - start + 1)
    return max_length


                      
print(longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
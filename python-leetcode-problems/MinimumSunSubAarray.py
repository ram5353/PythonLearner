def minimumSubArray(nums, sum):
    start = 0
    end = 0
    current_sum = 0
    min_length = float('inf')
    while end < len(nums):
        current_sum += nums[end]
        end += 1
        while start < end and sum <= current_sum:
            current_sum -= nums[start]
            start += 1
            min_length = min(min_length, end-start+1)
    return min_length


def maximumSumSubArray(nums, n):
    current_subarray = sum(nums[:n])
    result = []
    result.append(current_subarray)
    for i in range(1,len(nums)-n+1):
        current_subarray = current_subarray + nums[i+n-1] - nums[i-1]
        result.append(current_subarray)
    print(result)

def twoSumPairs(nums, k):
    nums.sort()
    start = 0
    end = len(nums) -1
    result = []
    while(start < end):
        if nums[start] + nums[end] == k:
            result.append([nums[start], nums[end]])
            start += 1
            end -= 1
        elif nums[start] + nums[end] < k:
            start += 1
        elif nums[start] + nums[end] > k:
            end -= 1
    return len(result)




print(twoSumPairs([4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4], 2))
maximumSumSubArray([1,2,3,4,5,6], 3)
print(minimumSubArray([1,2,3,4,5,6], 7))
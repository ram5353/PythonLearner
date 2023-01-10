def maxRob(nums, n):
    if n < 0:
        return 0
    return max(nums[n] + maxRob(n - 2), maxRob(n - 1))

def robRecursive(nums):
    n = len(nums)
    return maxRob(nums, n - 1)

def robDynamic(nums):
    dp = [-1 for _ in range(len(nums))]
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(nums[i] + dp[i-2], dp[i - 1])
    return dp[len(nums)-1]

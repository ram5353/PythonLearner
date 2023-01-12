def canPartition(nums):
    n = len(nums)
    total = sum(nums)
    if total%2 != 0:
        return False
    else:
        return recursion(nums, n, int(total/2))

def recursion(nums, n, sum):
    dp = [[False for _ in range(sum+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True
    for i in range(1, sum+1):
        dp[0][i] = False
    for i in range(1, n+1):
        for j in range(1, sum+1):
            if nums[i-1] <= j:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][sum]
             

print(canPartition([1,5,11,5]))
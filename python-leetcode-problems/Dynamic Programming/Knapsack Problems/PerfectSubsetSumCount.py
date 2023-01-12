def subsetSumCountRecursive(arr, sum):
    n = len(arr)
    count = 0
    return recursion(arr, sum, n, 0, count)

def recursion(arr, sum, n, i, count):
    if n == i:
        if sum == 0:
            count += 1
        return count
    count = recursion(arr, sum, n, i+1, count)
    count = recursion(arr, sum-arr[i], n, i+1, count)

def subsetSumCountMemoization(arr, sum):
    n = len(arr)
    dp =([[0 for _ in range(sum + 1)] 
            for _ in range(n + 1)])
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1, sum+1):
        dp[0][i] = 0
    for i in range(1, n+1):
        for j in range(1, sum + 1):
            if j < arr[i-1]:
                dp[i][j] = dp[i-1][j]
            if j >= arr[i-1]:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
    print(dp)
    return dp[n][sum]

print(subsetSumCountMemoization([1,2,3,4,5], 10))
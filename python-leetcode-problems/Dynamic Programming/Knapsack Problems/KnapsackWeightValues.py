def maxProfit(weights, values, w):
    n = len(weights)
    return recursion(weights, values, w, n)

def recursion(weights, values, w, n):
    if n == 0 or w == 0:
        return 0
    if weights[n-1] <= w:
        return max(values[n-1] + recursion(weights, values, w - weights[n-1], n-1), recursion(weights, values, w, n-1))
    else:
        return recursion(weights, values, w, n-1)

def memoization(weights, values, w, n):
    dp = [[-1 for _ in range(100)] for _ in range(1000)]
    if dp[n][w] != -1:
        return dp[n][w]
    if weights[n-1] <= w:
        dp[n][w] = max(values[n-1] + recursion(weights, values, w - weights[n-1], n-1), recursion(weights, values, w, n-1))
        return dp[n][w]
    else:
        dp[n][w] = recursion(weights, values, w, n-1)
        return dp[n][w]
    



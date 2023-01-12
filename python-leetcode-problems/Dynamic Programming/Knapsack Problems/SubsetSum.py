def subsetSum(arr, sum):
    n = len(arr)
    return recursive(arr, n, sum)

def recursive(arr, n, sum):
    if sum == 0:
        return True
    if n == 0:
        return False
    if arr[n-1] > sum:
        return recursive(arr, n-1, sum)
    return recursive(arr, n-1, sum) or recursive(arr, n-1, sum - arr[n-1])

def subsetSumMemoization(arr, sum):
    n = len(arr)
    subset =([[False for _ in range(sum + 1)] 
            for _ in range(len(arr) + 1)])
    for i in range(n+1):
        subset[i][0] = True
    for i in range(1, sum+1):
        subset[0][i] = False
    for i in range(1, n+1):
        for j in range(1, sum + 1):
            if j < arr[i-1]:
                subset[i][j] = subset[i-1][j]
            if j >= arr[i-1]:
                subset[i][j] = subset[i-1][j] or subset[i-1][j-arr[i-1]]
    return subset[n][sum]
    
print(subsetSum([3, 34, 4, 12, 5, 2], 9))
print(subsetSumMemoization([1,2,3,4,5], 10))


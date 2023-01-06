def recursive(costs, coins, n):
    if n == 0 or coins == 0:
        return 0
    if costs[n-1] <= coins:
        return max(1 + recursive(costs, coins-costs[n-1], n-1), recursive(costs, coins, n-1))
    elif costs[n-1] > coins:
        return recursive(costs, coins, n-1)

def maxIceCream(costs, coins):
    n = len(costs)
    return recursive(costs, coins, n)

print(maxIceCream([1,6,3,1,2,5], 20))

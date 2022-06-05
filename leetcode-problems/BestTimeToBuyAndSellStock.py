def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
    return max_profit

def maxProfitSlidingWindow(prices):
    l, r = 0, 0
    maxProfit = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxProfit = max(profit, maxProfit)
        else:
            l = r
        r += 1
    return maxProfit


print(maxProfit([7,1,5,3,6,4]))
print(maxProfitSlidingWindow([7,1,5,3,6,4]))
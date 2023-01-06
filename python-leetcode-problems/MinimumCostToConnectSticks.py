import heapq

def connectSticks(sticks):
    heapq.heapify(sticks)
    cost = 0
    while len(sticks) > 1:
        a = heapq.heappop(sticks)
        b = heapq.heappop(sticks)
        cost += a + b
        heapq.heappush(sticks, a + b)
    return cost

def connectSticksTest(sticks):
    heapq.heapify(sticks)
    print(sticks)

connectSticksTest([5,7,9,1,3])
    
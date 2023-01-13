import heapq


def lastStoneWeight(stones):
    stones = [-stones[i] for i in range(len(stones))]
    heapq.heapify(stones)
    while len(stones) > 1:
        stone1 = heapq.heappop(stones)
        stone2 = heapq.heappop(stones)
        if stone1 != stone2:
            heapq.heappush(stones, stone1-stone2)
    return -heapq.heappop(stones) if stones else 0
    
print(lastStoneWeight([1]))
        
import heapq


def lastStoneWeight(stones):
    heapq.heapify(stones)
    while len(stones) > 1:
        
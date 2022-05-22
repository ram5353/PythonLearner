def maximumBags(capacity, rocks, additionalRocks):
    result = 0
    for i, r in enumerate(rocks):
        capacity[i] -= r
    fill = sorted(capacity)
    for f in fill:
        if additionalRocks >= f:
            result += 1
            additionalRocks -= f
    return result





print(maximumBags([10, 2, 2], [2,2,0], 100))
# print(maximumBags([2,3,4,5], [1,2,4,4], 2))
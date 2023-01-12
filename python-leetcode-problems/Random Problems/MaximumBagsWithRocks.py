def maximumBags(capacity, rocks, additionalRocks):
        count = 0
        diff_array = [c-r for c,r in zip(capacity, rocks)]
        diff_array.sort()
        for element in diff_array:
            if element == 0:
                count += 1
            elif additionalRocks > 0:
                if element <= additionalRocks:
                    count += 1
                additionalRocks -= element
        return count

print(maximumBags([2,3,4,5], [1,2,4,4], 2))
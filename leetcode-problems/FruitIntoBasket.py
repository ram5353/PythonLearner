from collections import defaultdict


def totalFruit(fruits):
    start, end = 0, 0
    maximum = 0
    dict = {}
    while end < len(fruits):
        dict[fruits[end]] = end
        if len(dict) > 2:
            min_value = min(dict.values())
            del dict[fruits[min_value]]
            start = min_value + 1
        maximum = max(maximum, end - start + 1)
        end += 1
    return maximum





print(totalFruit([3,3,3,1,2,1,1,2,3,3,4]))
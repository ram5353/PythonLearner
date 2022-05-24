from collections import Counter


def uniqueOccurrences(arr):
    c = Counter(arr)
    if len(c.values()) == len(set(c.values())):
        return True
    else:
        return False

print(uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))

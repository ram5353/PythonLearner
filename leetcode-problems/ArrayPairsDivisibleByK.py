from collections import Counter


def canArrange(arr, k):
    count = Counter(x % k for x in arr)
    if 0 in count and count[0]%2 != 0:
        return False
    for c in count:
        if c > 0 and count[c] != count[k - c]:
            return False
    return True


print(canArrange([1,2,3,4,5,10,6,7,8,9], 5))

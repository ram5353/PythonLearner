from collections import Counter


def intersection(nums1, nums2):
    result = []
    sublist = [nums1[i:j] for i in range(0, len(nums1)) for j in range(i + 1, len(nums1))]
    print(sublist)
    for s in sublist:
        if set(s).issubset(set(nums2)):
            result.append(s)
    print(result)
    if len(result) == 0:
        return []
    return max(result, key=len)

def intersect(nums1, nums2):
    c = Counter(nums1)
    result = []
    for n in nums2:
        if c[n] > 0:
            result.append(n)
            c[n] -= 1
    return result









print(intersect([1,2,2,1], [2,2]))


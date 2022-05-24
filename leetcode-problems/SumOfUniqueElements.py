from collections import Counter


def sumOfUnique(nums) -> int:
    count = Counter(nums)
    sum = 0
    for c in count:
        if count[c] == 1:
            sum += c
    return sum


print(sumOfUnique([1,2,3,2]))
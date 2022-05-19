import collections
from collections import Counter

def majorityElement(nums):
    dictionary = {}
    for num in nums:
        if num not in dictionary:
            dictionary[num] = 1
        else:
            dictionary[num] += 1

    maximum = max(dictionary, key=dictionary.get)
    print(maximum)

def majority(nums):
    count = collections.Counter(nums)
    return max(count, key=count.get)


majorityElement([2,2,1,1,1])
majority([2,2,1,1,1])
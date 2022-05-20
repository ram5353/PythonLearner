import collections
def isMajorityElement(nums, target):
    count = collections.Counter(nums)
    maximum = max(count, key=count.get)
    return maximum == target and count[maximum] > len(nums)//2

print(isMajorityElement([10,100,101,101],101))


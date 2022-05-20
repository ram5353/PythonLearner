import collections
def majorityElement(nums):
    count = collections.Counter(nums)
    result = []
    for number in count:
        if count[number] > len(nums)//3:
            result.append(number)
    return result



print(majorityElement([1,2]))
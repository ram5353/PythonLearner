def containsDuplicate(nums: [int]) -> bool:
    if len(nums) > len(set(nums)):
        return True
    return False


def containsNearbyDuplicate(nums, k):

    for n in nums:
        count = nums.count(n)
        if count > 1:
            indices = [i for i, x in enumerate(nums) if x == n]
            for i in range(len(indices)):
                for j in range(i + 1, len(indices)):
                    diff = indices[j] - indices[i]
                    if diff <= k:
                        return True
    return False


def containsNearbyDuplicateOptimized(nums, k):
    dict = {}
    for i, n in enumerate(nums):
        if n in dict.keys():
            diff = i - dict[n]
            if diff <= k:
                return True
            dict[n] = i
        else:
            dict[n] = i
    return False


print(containsNearbyDuplicateOptimized([1,0,1,1],1))




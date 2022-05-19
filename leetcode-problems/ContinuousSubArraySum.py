import itertools

def continuous_sub_array_sum(nums, k):
    L = nums
    for i in range(0, len(L)):
        for j in range(i + 1, len(L) + 1):
            if len(L[i:j]) > 1 and sum(L[i:j]) % k == 0:
                return True
    return False

def optimized_continuous_sub_array_sum(nums, k):
    remainders = {0: -1}
    sum = 0
    for i, num in enumerate(nums):
        sum += num
        check_remainder = sum % k
        if check_remainder not in remainders.keys():
            remainders[check_remainder] = i
        elif i - remainders[check_remainder] > 1:
            return True
    return False


print(optimized_continuous_sub_array_sum([23,2,6,4,7], 13))
print(continuous_sub_array_sum([23,2,6,4,7], 13))


# Contigous
# import more_itertools
# print(list(more_itertools.substrings([0, 1, 2])))

# Non- Contiguous
# import more_itertools
# print(list(more_itertools.powerset([1,2,3,4])))
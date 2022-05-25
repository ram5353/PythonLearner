from collections import Counter


def countNicePairs(nums):
    result = 0
    MOD = 10**9 + 7
    count = Counter(n - reverse_number(n) for n in nums)
    for c in count.keys():
        count1 = count[c]
        result = (result + (count1*(count1-1))//2)%MOD
    return result


def reverse_number(number):
    number = str(number)
    re = "".join(reversed(number))
    return int(re)


print(countNicePairs([1, 10]))
import math


def longestSquareStreak(nums):
    nums.sort(reverse=True)
    seen = {}
    ans = -1

    for n in nums:
        if n*n in seen:
            seen[n] = seen[n*n]+1
            ans = max(ans, seen[n])
        else:
            seen[n] = 1

    return ans

print(longestSquareStreak([4,3,6,16,8,2]))

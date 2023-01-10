from collections import Counter


def distinctNumbers(nums, k):
    count = Counter(nums[:k])
    cur = len(count)
    ans = [cur]
    for i in range(k, len(nums)):
        count[nums[i-k]] -= 1
        if count[nums[i-k]] <= 0:
            del count[nums[i-k]]
        if count[nums[i]] == None:
            count[nums[i]] = 1
        else:
            count[nums[i]] += 1
        cur = len(count)
        ans.append(cur)
    return ans

print(distinctNumbers([1,2,3,2,2,1,3], 3))






def findLength(nums1, nums2):
    num2_str = ''.join([chr(n) for n in nums2])
    max_str = ''
    max_len = 0
    for n in nums1:
        max_str += chr(n)
        if max_str in num2_str:
            max_len = max(max_len, len(max_str))
        else:
            max_str = max_str[1:]
    return max_len

print(findLength([1,2,3,2,1], [3,2,1,4,7]))
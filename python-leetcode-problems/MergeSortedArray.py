def merge(nums1, n, nums2, m):
    # if m < 2:
    #     return nums1

    for value in nums2:
        nums1.insert(m,value)
        nums1.pop()
        m  += 1
    nums1.sort()
    return nums1

    

print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
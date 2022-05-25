def smallerNumbersThanCurrent(nums):
    sorted_list = sorted(nums)
    output = [0] * len(nums)
    for i, each in enumerate(nums):
        output[i] = sorted_list.index(each)
    return output

print(smallerNumbersThanCurrent([8,1,2,2,3]))
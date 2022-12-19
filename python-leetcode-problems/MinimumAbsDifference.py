import collections
import math


def minimumAbsDifference(arr):
    minDiff = math.inf
    dic = collections.defaultdict(list)
    print(dict)
    arr.sort()                                         
    for i in range(len(arr)-1):                        
        diff = arr[i+1] - arr[i]
        dic[diff].append([arr[i], arr[i+1]])           
        minDiff = min(minDiff, diff)
    return dic[minDiff]

print(minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))
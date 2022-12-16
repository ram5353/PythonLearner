def getWinner(arr, k):
    result = arr
    count = 0
    left_win = 0
    right_win = 0
    while count == 0:
        if (arr[0] > arr[1]):
            temp = arr[1]
            left_win += 1
            if left_win == k:
                return arr[0]
            right_win = 0
            arr.remove(arr[1])
            arr.append(temp)
        else:
            temp = arr[0]
            right_win += 1
            if right_win == k:
                return arr[1]
            left_win = 0
            arr.remove(arr[0])
            arr.append(temp)

print(getWinner([2,1,3,5,4,6,7], 2))
        

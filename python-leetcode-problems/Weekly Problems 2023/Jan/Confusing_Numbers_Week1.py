def confusingNumber(n):
    rotate = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
    result = ''
    for i in list(str(n)[::-1]):
        if i not in rotate.keys(): return False
        else: result += rotate[i]
    return int(result) != n


print(confusingNumber(8000))
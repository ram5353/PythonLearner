def plusOne(digits):
    check = ''.join(list(str(int(''.join(map(str, digits))) + 1)))
    print(check)
    
    #Alternative solution
    strs = [str(x) for x in digits]
    number = ''.join(strs)
    result = int(number) + 1
    print(result)
    return list(str(result))

print(plusOne([1,2,3]))
def isHappy(n: int):
    number = n
    stack = []
    while number != 1:
        total = 0
        for a in str(number):
            total += pow(int(a), 2)
        if total in stack:
            return False
        stack.append(total)
        number = total
    return True


print(isHappy(2))

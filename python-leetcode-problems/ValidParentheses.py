def isValid(s):
    if not s:
        return True
    dict = { ")": "(", "]": "[", "}": "{" }
    result = []
    for ch in s:
        if ch == '(' or ch == '{' or ch == '[':
            result.append(ch)
        else:
            if not result:
                return False
            comp = result.pop()
            if dict[ch] != comp:
                return False
    return not result


print(isValid("()[]{}"))



def isValid(s: str):
    stack = []
    mapping = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    for character in s:
        if character in mapping:
            if stack and stack[-1] == mapping[character]:
                stack.pop()
            else:
                return False
        else:
            stack.append(character)
    return not stack




print(isValid("([])"))

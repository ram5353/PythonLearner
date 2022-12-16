from itertools import product


def letterCombination(digits):
    dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    result = []
    chars = [dict[digit] for digit in digits]
    combs = product(*chars)
    for comb in combs:
        temp = ''.join(comb)
        result.append(temp)
    return result


print(letterCombination('234'))

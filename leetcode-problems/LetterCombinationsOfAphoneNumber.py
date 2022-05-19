from itertools import product

def letterCombinations(digits):
    numbers = {"2": "abc",
               "3": "def",
               "4": "ghi",
               "5": "jkl",
               "6": "mno",
               "7": "pqrs",
               "8": "tuv",
               "9": "wxyz"
               }
    my_list = []
    if digits == "":
        return []
    for digit in digits:
        my_list.append(numbers[digit])

    final = [''.join(s) for s in product(*my_list)]
    return final

def letterCombinations1(digits):
    numbers = {"2": "abc",
               "3": "def",
               "4": "ghi",
               "5": "jkl",
               "6": "mno",
               "7": "pqrs",
               "8": "tuv",
               "9": "wxyz"
               }
    result = list(numbers[digits[0]])
    for digit in digits[1:]:
        result = [old + new for old in result for new in list(numbers[digit])]
    return result


print(letterCombinations("23"))
print(letterCombinations1("23"))

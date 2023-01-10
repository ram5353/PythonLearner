def romanToInt(s):
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    totalSum = 0
    for i, roman in enumerate(s):
        if i < len(s) - 1:
            first = dict[s[i]]
            second = dict[s[i+1]]
            if first < second:
                totalSum -= first
            else:
                totalSum += first
    totalSum += dict[s[len(s) - 1]]
    return totalSum


print(romanToInt('III'))


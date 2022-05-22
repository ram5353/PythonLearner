def percentageLetter(s, letter):
    if letter in s:
        count = s.count(letter)
        result = int((count/len(s)) * 100)
        return result
    else:
        return 0


print(percentageLetter("sgawtb", "s"))
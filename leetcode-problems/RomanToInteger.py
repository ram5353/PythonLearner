def roman_to_int(s: str):
    sum = 0
    dictionary = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    for i, letter in enumerate(s):
        if i > 0 and dictionary[s[i]] > dictionary[s[i-1]]:
            sum += dictionary[s[i]] - (2 * dictionary[s[i-1]])
        else:
            sum += dictionary[s[i]]
    print(sum)

roman_to_int("MCMXCIV")
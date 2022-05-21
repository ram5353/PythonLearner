import sys
from collections import Counter


def firstUniqChar(s):
    c = Counter(s)
    first = sys.maxsize
    if 1 not in c.values():
        return -1
    for letter in c:
        if c[letter] == 1:
            first = min(first, s.index(letter))
    return first





print(firstUniqChar("loveleetcode"))
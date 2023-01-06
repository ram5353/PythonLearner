# You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.

# Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.

 

# Example 1:

# Input: s = "aabaaaacaabc", k = 2
# Output: 8
# Explanation: 
# Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
# Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
# A total of 3 + 5 = 8 minutes is needed.
# It can be proven that 8 is the minimum number of minutes needed.

def takeCharacters(s, k):
    # count = {'a': 0, 'b': 0, 'c': 0}
    # left = 0
    # right = len(s) - 1
    # while left <= right:
    #     count[s[left]] += 1
    #     count[s[right]] += 1
    #     if count['a'] >= k and count['b'] >= k and count['c'] >= k:
    #         return left + len(s) - right
    #     left += 1
    #     right -= 1
    # return -1
    left = 0
    right = len(s) - 1
    # Initialize a dictionary to store the count of each character
    count = {'a': 0, 'b': 0, 'c': 0}
    # Initialize the number of minutes to 0
    minutes = 0
    # Loop until the pointers meet
    while left <= right:
        # Increment the count of the character at the left pointer
        count[s[left]] += 1
        # Increment the count of the character at the right pointer
        count[s[right]] += 1
        # Increment the number of minutes
        minutes += 1
        # If we have at least k of each character, return the number of minutes
        if count['a'] >= k and count['b'] >= k and count['c'] >= k:
            return minutes
        # If we don't have at least k of each character, move one of the pointers towards the other
        if left < right:
            left += 1
        else:
            right -= 1
    # If we reach here, it means we couldn't find at least k of each character
    return -1

print(takeCharacters("aabaaaacaabc", 2))
    
# Take K of Each Character From Left and Right
# User Accepted:867
# User Tried:1601
# Total Accepted:873
# Total Submissions:3337
# Difficulty:Medium
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
    # Initialize left and right pointers
    left = 0
    right = len(s) - 1
    
    # Initialize counts of each character to 0
    counts = {'a': 0, 'b': 0, 'c': 0}
    
    # Initialize the number of minutes taken to 0
    minutes = 0
    
    # Iterate until we have taken at least k of each character
    while left <= right and (counts['a'] <= k or counts['b'] <= k or counts['c'] <= k):
        # Check which character occurs more frequently in the remaining portion of the string
        if s[left:right+1].count('a') >= s[left:right+1].count('c'):
            # Take the character from the left
            counts[s[left]] += 1
            left += 1
        else:
            # Take the character from the right
            counts[s[right]] += 1
            right -= 1
        # Increment the number of minutes taken
        minutes += 1
    
    # Return the number of minutes taken if we have taken k of each character, or -1 if not
    return minutes if counts['a'] >= k and counts['b'] >= k and counts['c'] >= k else -1

print(takeCharacters("aabaaaacaabc", 2))

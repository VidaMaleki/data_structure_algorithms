"""Example Problem: Longest Substring Without Repeating Characters 💡 Problem: Given a string s, find the length of the longest substring without repeating characters.
"""

#Sliding Window Solution (O(N)):
def longest_unique_substring(s):
    char_index = {}
    max_length, start = 0, 0
    
    for end in range(len(s)):
        if s[end] in char_index:
            start = max(start, char_index[s[end]] + 1)
        char_index[s[end]] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length

s = "abcabcbb"
print(longest_unique_substring(s))  # Output: 3 ("abc")

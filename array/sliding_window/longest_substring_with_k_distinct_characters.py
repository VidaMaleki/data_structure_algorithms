"""Example Problem: Longest Substring with K Distinct Characters 💡 Problem: Given a string s, find the length of the longest substring containing at most k distinct characters.
"""

#Sliding Window Solution (O(N)):
def longest_k_distinct(s, k):
    char_count = {}
    max_length, start = 0, 0

    for end in range(len(s)):
        char_count[s[end]] = char_count.get(s[end], 0) + 1

        while len(char_count) > k:
            char_count[s[start]] -= 1
            if char_count[s[start]] == 0:
                del char_count[s[start]]
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length

s = "araaci"
k = 2
print(longest_k_distinct(s, k))  # Output: 4 ("araa")

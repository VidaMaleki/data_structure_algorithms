"""Example Problem: Permutation in String 💡 Problem: Given two strings s1 and s2, return True if s1’s permutation is a substring of s2.
"""


#Sliding Window + Frequency Count Solution (O(N)):

from collections import Counter

def check_inclusion(s1, s2):
    s1_count, window_count = Counter(s1), Counter()
    start = 0
    
    for end in range(len(s2)):
        window_count[s2[end]] += 1

        if end >= len(s1) - 1:
            if window_count == s1_count:
                return True
            window_count[s2[start]] -= 1
            if window_count[s2[start]] == 0:
                del window_count[s2[start]]
            start += 1

    return False

s1 = "ab"
s2 = "eidbaooo"
print(check_inclusion(s1, s2))  # Output: True

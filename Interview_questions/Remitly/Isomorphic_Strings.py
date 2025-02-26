"""205. Isomorphic Strings
Easy
Topics
Companies
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "foo", t = "bar"

Output: false

Explanation:

The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:

Input: s = "paper", t = "title"

Output: true

 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character."""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False  # Edge case: different lengths
        
        s_to_t = {}  # Dictionary to map s -> t
        mapped_chars = set()  # Set to track already mapped characters in t
        
        for char_s, char_t in zip(s, t):
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False  # If already mapped, check if consistent
            else:
                if char_t in mapped_chars:
                    return False  # If char_t is already mapped by another char_s
                s_to_t[char_s] = char_t
                mapped_chars.add(char_t)
        
        return True

# Example Test Cases
solution = Solution()
print(solution.isIsomorphic("egg", "add"))  # Output: True
print(solution.isIsomorphic("foo", "bar"))  # Output: False
print(solution.isIsomorphic("paper", "title"))  # Output: True


"""
Explanation:
For s = "egg", t = "add":

s	t	Mapping (s_to_t)	mapped_chars
e	a	{e → a}	            {a}
g	d	{e → a, g → d}	    {a, d}
g	d	Valid match	        {a, d}
✅ Output: True

For s = "foo", t = "bar":

s	t	Mapping (s_to_t)	mapped_chars
f	b	{f → b}	            {b}
o	a	{f → b, o → a}	    {b, a}
o	r	❌ Conflict: o → a but found o → r	
❌ Output: False

Time & Space Complexity:
Time Complexity: 
O(n) (Iterates through s and t once)
Space Complexity: 
O(1) (At most 256 unique ASCII characters)"""
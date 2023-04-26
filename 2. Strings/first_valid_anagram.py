# https://leetcode.com/problems/contains-duplicate/
# My submission: https://leetcode.com/problems/valid-anagram/submissions/939791343/
# leetcode stats
# Runtime: 32ms, beats 98.31%
# memory: 14.3mb, beats 94.34%
"""
>>> is_anagram(s = "anagram", t = "nagaram")
True
>>> is_anagram(s = "rat", t = "car")
False
"""
from collections import Counter
def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
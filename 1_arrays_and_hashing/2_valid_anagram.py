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


### outside leetcode ###
"""
>>> is_valid("abacate","acabate")
True
>>> is_valid("boia", "baio")
True
>>> is_valid("sapo", "pazo")
False
>>> is_valid_2("abacate","acabate")
True
>>> is_valid_2("sapo", "pazo")
False
"""


def is_valid(a, b):
    return sorted(a) == sorted(b)


def is_valid_2(a, b):
    sign_a = [0] * 26  # [0,0,0,0,0,0,0]
    sign_b = [0] * 26
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        sign_a[ord(a[i]) - ord("a")] += 1
        sign_b[ord(b[i]) - ord("a")] += 1
    # print(sign_a)
    # print(sign_b)
    return sign_a == sign_b


if __name__ == "__main__":
    import timeit
    import doctest

    doctest.testmod()
    print(timeit.timeit(lambda: is_valid_2("abacate", "acatabe")))
    print(timeit.timeit(lambda: is_valid("abacate", "acatabe")))

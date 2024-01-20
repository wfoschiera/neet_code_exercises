# https://leetcode.com/problems/group-anagrams/

"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

>>> group_anagrams(["eat","tea","tan","ate","nat","bat"])
[['bat'],['nat','tan'],['ate','eat','tea']]
>>> group_anagrams([""])
[['']]
>>> group_anagrams(["a"])
[['a']]
"""
from collections import defaultdict


def group_anagrams(a):
    if a == [""]:
        return [[""]]
    res = defaultdict(list)
    for word in a:
        key = "".join(sorted(word))
        res[key].append(word)
    return list(res.values())


# def is_valid(a, b):
#     return sorted(a) == sorted(b)

# def group_anagrams_2(word_list):
#     res = defaultdict(list)
#     for word1 in word_list:
#         for word2 in word_list:
#             if is_valid(word1, word2):


# #### NEET CODE  ####
# def groupAnagrams(strs: List[str]) -> List[List[str]]:
#     ans = collections.defaultdict(list)

#     for s in strs:
#         count = [0] * 26
#         for c in s:
#             count[ord(c) - ord("a")] += 1
#         ans[tuple(count)].append(s)
#     return ans.values()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

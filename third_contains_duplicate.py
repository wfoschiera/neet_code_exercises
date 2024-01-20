# https://leetcode.com/problems/contains-duplicate/
# My submission: https://leetcode.com/problems/contains-duplicate/submissions/939257729/
# leetcode stats
# Runtime: 551ms, beats 74.84%
# memory: 28.7mb, beats 77.50%
"""
>>> contains_duplicate([1,2,3,1])
True
>>> contains_duplicate([1,2,3,4])
False
>>> contains_duplicate([1,1,1,3,3,4,3,2,4,2])
True
"""


def contains_duplicate(nums: list[int]) -> bool:
    # leverages from python set
    # another way is to iterate over nums adding to a set and verifying if the element
    # is already in the set
    return len(nums) != len(set(nums))

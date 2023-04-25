# https://leetcode.com/problems/two-sum/
# My submission: https://leetcode.com/problems/two-sum/submissions/939254862/
# leetcode stats
# Runtime: 60ms, beats 80.20%
# memory: 15.4mb, beats 5.81%
"""
>>> two_sum([2,7,11,15], 9)
[0, 1]
>>> two_sum([3,2,4], 6)
[1, 2]
>>> two_sum([3,3], 6)
[0, 1]
"""

def two_sum(nums: list[int], target: int) -> list[int]:
    # creates a hashmap to improve performance, see dict in
    # doc https://wiki.python.org/moin/TimeComplexity
    target_map = {}
    for i, num in enumerate(nums):
        diff = target - num
        complement = target_map.get(num)
        if complement is not None:
            return [complement,i]
        target_map[diff] = i

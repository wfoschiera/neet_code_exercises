# https://leetcode.com/problems/two-sum/
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


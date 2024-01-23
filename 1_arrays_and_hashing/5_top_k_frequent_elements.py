# https://leetcode.com/problems/top-k-frequent-elements/description/
# My submission: https://leetcode.com/problems/top-k-frequent-elements/submissions/1151954663
# leetcode stats
# Runtime: 83, beats 93.94%
# memory: 21.00mb, beats 94.43%


from collections import Counter


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """all my own"""
    freq = Counter(nums)
    ordered = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    ordered_list = [x[0] for x in ordered]
    return ordered_list[:k]


nums = [1, 1, 1, 2, 2, 3]
k = 2
expected = [1, 2]
assert top_k_frequent(nums, k) == expected


def sol2(nums, k):
    """based on other responses"""
    return [x[0] for x in Counter(nums).most_common(k)]


assert sol2(nums, k) == expected

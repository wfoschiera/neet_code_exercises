# https://leetcode.com/problems/product-of-array-except-self/description/
# My submission: https://leetcode.com/problems/product-of-array-except-self/submissions/1154154086
# leetcode stats
# Runtime: 159, beats 93.20%
# memory: 23.65mb, beats 93.99%

"""
>>> nums = [1,2,3,4]
>>> assert product_except_self(nums) == [24, 12, 8, 6]
>>> nums = [-1,1,0,-3,3]
>>> assert product_except_self(nums) == [0,0,9,0,0]
"""


def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    output = [1] * n

    p = 1
    for i in range(n):
        output[i] = p
        p *= nums[i]

    p = 1
    for i in range(n - 1, -1, -1):
        output[i] *= p
        p *= nums[i]
    return output

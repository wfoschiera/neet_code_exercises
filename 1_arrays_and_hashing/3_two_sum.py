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
            return [complement, i]
        target_map[diff] = i


two_sum([2, 7, 11, 15], 9)


### outside leetcode ###
def two_sum(nums, target):
    for i, v in enumerate(nums):
        for j, h in enumerate(nums):
            if i == j:
                continue
            if v + h == target:
                print(i, j)
                return


two_sum([2, 7, 11, 15], 9)


def two_sum2(nums, target):
    num_map = {}
    for i, v in enumerate(nums):
        comp = target - v
        if num_map[v]:
            print("v:", v)
            print("get: ", num_map.get(v))
            return [num_map[v], i]
        num_map[comp] = i


print(two_sum2([3, 5, 9, 5], 8))
# {5: [0], 3:[1], -1: [2], 3: [3]}

print(two_sum2([4, 5, 9, 5], 8))

print(two_sum2([4, 3, 9, 5], 14) == [2, 3])
print(two_sum2([4, 4, 4, 4], 8))


"""
Dado um array de inteiros nums e um inteiro target, retorne os indices dos dois numeros que somados são iguais ao target,
Pode assumir que pra cada entrada vai existir exatamente uma solução e você não pode usar duas vezes o mesmo elemento.
Example 1:


Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Como nums[0] + nums[1] == 9, retornamos [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

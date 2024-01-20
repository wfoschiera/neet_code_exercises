# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# My submission: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/939253420/
# leetcode stats
# Runtime: 939ms, beats 90.26%
# memory: 24.9mb, beats 96.83%
"""
>>> max_profit([7,1,5,3,6,4])
5
>>> max_profit([7,6,4,3,1])
0
>>> max_profit([2,4,1])
2
"""


def max_profit(prices: list[int]) -> int:
    min_price = float("inf")
    max_price = float("-inf")
    best_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
            # trick to restart profit calculus on next iteration.
            # Avoid to run all over the array again
            max_price = float("-inf")
        elif price > max_price:
            max_price = price
        if max_price > min_price:
            profit = max_price - min_price
            if profit > best_profit:
                best_profit = profit
    return best_profit

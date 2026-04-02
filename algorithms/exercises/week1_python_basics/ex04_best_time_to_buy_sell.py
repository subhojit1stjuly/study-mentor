# Exercise 04 — Best Time to Buy and Sell Stock
# Difficulty: Easy
# Topic: Sliding Window / Greedy thinking
#
# TASK:
#   You are given a list of prices where prices[i] is the price of a
#   stock on day i.
#
#   You want to maximize your profit by choosing:
#     - ONE day to BUY
#     - ONE LATER day to SELL
#
#   Return the maximum profit you can achieve.
#   If no profit is possible, return 0.
#
# RULES:
#   - You must buy BEFORE you sell (earlier index = earlier day)
#   - You can only hold one transaction (one buy, one sell)
#   - Do NOT use a nested loop — aim for O(n)
#
# EXAMPLES:
#   max_profit([7, 1, 5, 3, 6, 4])  → 5   (buy at 1, sell at 6)
#   max_profit([7, 6, 4, 3, 1])     → 0   (prices only go down, no profit)
#   max_profit([2, 4, 1])           → 2   (buy at 2, sell at 4)
#
# Time Complexity goal: O(n)
# Space Complexity goal: O(1)
#
# THINK ABOUT IT FIRST:
#   As you walk through the prices day by day, what two things
#   do you need to keep track of?
#   (Don't read below until you've thought for a few minutes)
#
# HINT (only if stuck after 10 minutes):
#   Track two things as you scan left to right:
#     1. The LOWEST price seen so far (best day to have bought)
#     2. The BEST profit seen so far
#   At each day: what's my profit IF I sold today?
#   Is that better than my best profit so far?


def max_profit(prices: list[int]) -> int:
    left = 0
    right = 1
    profit = 0
    while left < right and right < len(prices) :
        current_profit = prices[right] - prices[left]
        if current_profit > profit :
            profit = current_profit
        if prices[left] > prices[right]:
            left = right
        right += 1        
    return profit
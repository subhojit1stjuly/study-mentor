# Exercise 02 — Two Sum
# Difficulty: Easy (Classic Interview Problem)
# Topic: Lists, Loops, Dictionaries
#
# TASK:
#   Given a list of integers and a target number,
#   return the INDICES of the two numbers that add up to target.
#   You may assume exactly one solution exists.
#   You cannot use the same element twice.
#
# RULES:
#   - Return a list with two indices: [i, j]
#   - Order doesn't matter: [0, 1] and [1, 0] are both acceptable
#   - Do NOT use a nested loop (that would be O(n²)) — aim for O(n)
#
# EXAMPLES:
#   two_sum([2, 7, 11, 15], 9)   → [0, 1]  (because 2 + 7 = 9)
#   two_sum([3, 2, 4], 6)        → [1, 2]  (because 2 + 4 = 6)
#   two_sum([3, 3], 6)           → [0, 1]  (because 3 + 3 = 6)
#
# Time Complexity goal: O(n)
# Space Complexity goal: O(n)
#
# HINT (only read if stuck after 10 minutes):
#   For each number you see, ask yourself:
#   "What number would I need to pair with this to reach the target?"
#   If you've seen that number before... you found your pair.
#   What data structure lets you check "have I seen this before?" in O(1)?


def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i,num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [i,seen[complement]]
        seen[num] = i
    return []
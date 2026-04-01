# Exercise 01 — Find Maximum
# Difficulty: Easy (Python Warm-up)
# Topic: Loops, Variables
#
# TASK:
#   Write a function that takes a list of integers and returns
#   the largest number in the list.
#
# RULES:
#   - Do NOT use Python's built-in max() function
#   - Use a loop
#   - You can assume the list is non-empty
#
# EXAMPLES:
#   find_max([3, 1, 4, 1, 5, 9])  → 9
#   find_max([-5, -2, -8])        → -2
#   find_max([7])                 → 7
#
# Time Complexity goal: O(n)
# Space Complexity goal: O(1)


def find_max(nums: list[int]) -> int:
    max_num = nums[0]
    for num in nums:
        if num>max_num:
            max_num = num
    return max_num        
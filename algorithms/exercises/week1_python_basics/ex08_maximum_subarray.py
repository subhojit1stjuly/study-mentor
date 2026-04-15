# Exercise 08 — Maximum Subarray
# Difficulty: Medium
# Topic: ??? (identify the pattern yourself)
#
# TASK:
#   Given an integer array nums, find the subarray with the
#   largest sum and return that sum.
#
# RULES:
#   - A subarray is contiguous (no skipping elements)
#   - Aim for O(n) — no nested loops
#   - The array may contain negative numbers
#
# EXAMPLES:
#   max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])  → 6  (subarray [4,-1,2,1])
#   max_subarray([1])                                → 1
#   max_subarray([5, 4, -1, 7, 8])                  → 23 (whole array)
#
# Time Complexity goal: O(n)
# Space Complexity goal: O(1)
#
# THINK BEFORE YOU CODE:
#   As you walk through the array, you're building a running sum.
#   At each element, you have a choice:
#     A) Extend the current subarray: running_sum + nums[i]
#     B) Start fresh from nums[i] (abandon everything before)
#
#   When is option B better than option A?
#   What does that tell you about when to "reset" your running sum?
#   [-3,-1,-2]

def max_subarray(nums: list[int]) -> int:
    running_sum = 0
    best = nums[0]
    for i in range(len(nums)):
        running_sum = max(nums[i], running_sum + nums[i])
        best = max(best,running_sum)
    return best

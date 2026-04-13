# Exercise 07 — Product of Array Except Self
# Difficulty: Medium
# Topic: ??? (figure out the pattern — no hints)
#
# TASK:
#   Given an integer array nums, return an array answer such that
#   answer[i] is the product of all elements EXCEPT nums[i].
#
# RULES:
#   - Do NOT use division
#   - Aim for O(n) time
#   - The output array does NOT count as extra space
#
# EXAMPLES:
#   product_except_self([1, 2, 3, 4])   → [24, 12, 8, 6]
#   product_except_self([-1, 1, 0, -3, 3])  → [0, 0, 9, 0, 0]
#
# Time Complexity goal: O(n)
# Space Complexity goal: O(1) extra (output array doesn't count)
#
# VERIFY THE FIRST EXAMPLE MANUALLY:
#   answer[0] = 2 * 3 * 4 = 24  (everything except index 0)
#   answer[1] = 1 * 3 * 4 = 12  (everything except index 1)
#   answer[2] = 1 * 2 * 4 = 8   (everything except index 2)
#   answer[3] = 1 * 2 * 3 = 6   (everything except index 3)
#
# THINK BEFORE YOU CODE:
#   For answer[i], you need: (product of everything LEFT of i)
#                          * (product of everything RIGHT of i)
#
#   Can you compute the LEFT products for all positions in one pass?
#   Then can you multiply in the RIGHT products in a second pass?
#   What single variable do you need to carry through each pass?


def product_except_self(nums: list[int]) -> list[int]:
    answer = [1] * len(nums)
    running = 1
    for i in range(len(nums)):
        answer[i] = running
        running *= nums[i]
    running =  1
    for i in range(len(nums)-1,-1,-1):
        answer[i] *= running
        running *= nums[i]
    return answer
    

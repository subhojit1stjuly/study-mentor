# Exercise 06 — Container With Most Water
# Difficulty: Medium
# Topic: ??? (figure it out — no hints on the pattern)
#
# TASK:
#   You are given a list of n integers called height.
#   There are n vertical lines drawn such that the two endpoints of
#   the i-th line are at (i, 0) and (i, height[i]).
#
#   Find two lines that together with the x-axis form a container
#   that holds the MOST water. Return the maximum area.
#
#   Area = min(height[left], height[right]) * (right - left)
#          ↑ the shorter wall is the bottleneck
#
# RULES:
#   - Do NOT use a nested loop — O(n) solution exists
#   - You may not slant the container
#
# EXAMPLES:
#   max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])  → 49
#   max_area([1, 1])                         → 1
#   max_area([4, 3, 2, 1, 4])               → 16
#   max_area([1, 2, 1])                      → 2
#
# Time Complexity goal: O(n)
# Space Complexity goal: O(1)
#
# THINK BEFORE YOU CODE:
#   Start with pointers at both ends — the widest possible container.
#   Width shrinks as pointers move inward.
#   To have any chance of more area, what must increase?
#   Which pointer should you move — the taller one or the shorter one? Why?


def max_area(height: list[int]) -> int:
    area,left,right = 0,0,len(height)-1
    while left < right:
        area = max(area,min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -=1

    return area

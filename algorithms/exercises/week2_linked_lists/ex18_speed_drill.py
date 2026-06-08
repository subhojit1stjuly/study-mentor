# Exercise 18 — Speed Drill
# ============================================================
# 10 rapid-fire problems. Focus on speed + accuracy.
# Time yourself: can you identify all patterns in 5 minutes?
# Then implement them.
# ============================================================


# ── Problem 1 ────────────────────────────────────────────────
# LeetCode 217: https://leetcode.com/problems/contains-duplicate/
# (Similar: check if all characters are unique)
#
# Check if a string has all unique characters (no repeats).
#
# is_unique("abcdef")  → True
# is_unique("hello")   → False

# Pattern:
def is_unique(s: str) -> bool:
    pass


# ── Problem 2 ────────────────────────────────────────────────
# LeetCode 26: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
#
# Given a sorted array, remove duplicates in-place and return
# the new length.
#
# remove_duplicates([1,1,2])  → 2

# Pattern:
def remove_duplicates(nums: list[int]) -> int:
    pass


# ── Problem 3 ────────────────────────────────────────────────
# LeetCode 643: https://leetcode.com/problems/maximum-average-subarray-i/
# (Similar: find max sum instead of average)
#
# Find the maximum sum of any subarray of size k.
#
# max_sum_k([2,1,5,1,3,2], k=3)  → 9  ([5,1,3])

# Pattern:
def max_sum_k(nums: list[int], k: int) -> int:
    pass


# ── Problem 4 ────────────────────────────────────────────────
# LeetCode 53: https://leetcode.com/problems/maximum-subarray/
#
# Given an array, find the maximum sum subarray.
#
# max_subarray([-2,1,-3,4,-1,2,1,-5,4])  → 6  ([4,-1,2,1])

# Pattern:
def max_subarray(nums: list[int]) -> int:
    pass


# ── Problem 5 ────────────────────────────────────────────────
# LeetCode 155: https://leetcode.com/problems/min-stack/
#
# Implement a MinStack — a stack that supports push, pop, top,
# and retrieving the minimum element in O(1).

# Pattern:
class MinStack:
    def __init__(self):
        pass
    
    def push(self, val: int) -> None:
        pass
    
    def pop(self) -> None:
        pass
    
    def top(self) -> int:
        pass
    
    def get_min(self) -> int:
        pass


# ── Problem 6 ────────────────────────────────────────────────
# LeetCode 876: https://leetcode.com/problems/middle-of-the-linked-list/
#
# Find the middle node of a linked list in one pass.

# Pattern:
def find_middle(head: 'ListNode') -> 'ListNode':
    pass


# ── Problem 7 ────────────────────────────────────────────────
# LeetCode 34: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
#
# Given a sorted array, find the first and last position of target.
# Return [-1,-1] if not found.
#
# search_range([5,7,7,8,8,10], 8)  → [3,4]

# Pattern:
def search_range(nums: list[int], target: int) -> list[int]:
    pass


# ── Problem 8 ────────────────────────────────────────────────
# LeetCode 287: https://leetcode.com/problems/find-the-duplicate-number/
#
# Given an array with one duplicate number, find it.
# Array contains n+1 integers from 1 to n.
#
# find_duplicate([1,3,4,2,2])  → 2

# Pattern:
def find_duplicate(nums: list[int]) -> int:
    pass


# ── Problem 9 ────────────────────────────────────────────────
# LeetCode 346: https://leetcode.com/problems/moving-average-from-data-stream/
#
# Design a data structure that supports adding numbers
# and finding the average of the last k numbers added.

# Pattern:
class MovingAverage:
    def __init__(self, size: int):
        pass
    
    def next(self, val: int) -> float:
        pass


# ── Problem 10 ───────────────────────────────────────────────
# LeetCode 560: https://leetcode.com/problems/subarray-sum-equals-k/
#
# Find the number of continuous subarrays that sum to k.
#
# subarray_sum([1,1,1], k=2)  → 2

# Pattern:
def subarray_sum(nums: list[int], k: int) -> int:
    pass

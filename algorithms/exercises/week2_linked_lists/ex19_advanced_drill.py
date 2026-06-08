# Exercise 19 — Advanced Pattern Drill
# ============================================================
# 8 problems focusing on the trickier patterns.
# These are the ones that separate intermediate from advanced:
# - Kadane's variants
# - Floyd's Cycle Detection
# - Prefix Sum + Hash Map
# - Binary Search variants
# ============================================================


# ── Problem 1 ────────────────────────────────────────────────
# LeetCode 918: https://leetcode.com/problems/maximum-sum-circular-subarray/
#
# Maximum Circular Subarray Sum
# Given a circular array, find the maximum sum subarray.
# (The array wraps around — last element connects to first)
#
# max_circular_sum([1,-2,3,-2])       → 3
# max_circular_sum([5,-3,5])          → 10  (5+5, wrapping)
# max_circular_sum([-2,-3,-1])        → -1
#
# Hint: Max can be in the middle OR wrap around the edges.
#       If wrapping, max = total - (min subarray sum)

# Pattern:
def max_circular_sum(nums: list[int]) -> int:
    pass

# Time:  O(?)
# Space: O(?)


# ── Problem 2 ────────────────────────────────────────────────
# LeetCode 628: https://leetcode.com/problems/maximum-product-of-three-numbers/
#
# Maximum Product of Three Numbers
# Given an array, return the maximum product of any three numbers.
#
# max_product_three([1,2,3])           → 6
# max_product_three([-10,-10,1,3,2])  → 300  (-10*-10*3)
# max_product_three([-100,-98,-1,2,3,4]) → 39200  (-100*-98*4)
#
# Hint: Either three largest OR two smallest * one largest

# Pattern:
def max_product_three(nums: list[int]) -> int:
    pass

# Time:  O(?)
# Space: O(?)


# ── Problem 3 ────────────────────────────────────────────────
# LeetCode 287: https://leetcode.com/problems/find-the-duplicate-number/
#
# Find the Duplicate Number (must use O(1) space)
# Array contains n+1 integers from 1 to n.
# Exactly one number appears twice.
# You cannot modify the array.
#
# find_duplicate([1,3,4,2,2])      → 2
# find_duplicate([3,1,3,4,2])      → 3
#
# Hint: Treat values as "next pointers" — index i points to nums[i]

# Pattern:
def find_duplicate(nums: list[int]) -> int:
    pass

# Time:  O(?)
# Space: O(?)


# ── Problem 4 ────────────────────────────────────────────────
# LeetCode 523: https://leetcode.com/problems/continuous-subarray-sum/
#
# Continuous Subarray Sum
# Given an array and an integer k, return True if there exists
# a subarray of length >= 2 that sums to a multiple of k.
#
# check_subarray_sum([23,2,4,6,7], k=6)   → True  ([2,4] sums to 6)
# check_subarray_sum([23,2,6,4,7], k=6)   → True  ([23,2,6,4,7] sums to 42)
# check_subarray_sum([23,2,4,6,7], k=13)  → False
#
# Hint: (prefix[j] - prefix[i]) % k == 0 means prefix[j] % k == prefix[i] % k

# Pattern:
def check_subarray_sum(nums: list[int], k: int) -> bool:
    pass

# Time:  O(?)
# Space: O(?)


# ── Problem 5 ────────────────────────────────────────────────
# LeetCode 974: https://leetcode.com/problems/subarray-sums-divisible-by-k/
# (Similar: find length instead of count)
#
# Longest Subarray with Sum Divisible by K
# Given an array, find the length of the longest subarray
# whose sum is divisible by k.
#
# longest_divisible([2,7,6,1,4,5], k=3)  → 4  ([7,6,1,4] sums to 18)
# longest_divisible([1,2,3], k=5)        → 0

# Pattern:
def longest_divisible(nums: list[int], k: int) -> int:
    pass

# Time:  O(?)
# Space: O(?)


# ── Problem 6 ────────────────────────────────────────────────
# LeetCode 81: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
#
# Search in Rotated Sorted Array II (with duplicates)
# Array was sorted, then rotated. May contain duplicates.
# Return True if target exists.
#
# search([2,5,6,0,0,1,2], 0)  → True
# search([2,5,6,0,0,1,2], 3)  → False
# search([1,0,1,1,1], 0)      → True
#
# Hint: When nums[mid] == nums[left], you can't tell which half is sorted

# Pattern:
def search(nums: list[int], target: int) -> bool:
    pass

# Time:  O(?)
# Space: O(?)


# ── Problem 7 ────────────────────────────────────────────────
# LeetCode 658: https://leetcode.com/problems/find-k-closest-elements/
#
# Find K Closest Elements
# Given a sorted array, find the k elements closest to x.
# Return them in sorted order.
#
# find_closest([1,2,3,4,5], k=4, x=3)  → [1,2,3,4]
# find_closest([1,2,3,4,5], k=4, x=-1) → [1,2,3,4]
#
# Hint: Binary search to find the starting position of the k-window

# Pattern:
def find_closest(arr: list[int], k: int, x: int) -> list[int]:
    pass

# Time:  O(?)
# Space: O(?)


# ── Problem 8 ────────────────────────────────────────────────
# LeetCode 1031: https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/
#
# Maximum Sum of Two Non-Overlapping Subarrays
# Given an array, find the maximum sum of two non-overlapping
# subarrays with lengths L and M.
#
# max_sum_two([0,6,5,2,2,5,1,9,4], L=1, M=2)  → 20  ([9] + [6,5])
# max_sum_two([3,8,1,3,2,1,8,9,0], L=3, M=2)  → 29  ([3,8,1] + [8,9])
#
# Hint: Prefix sums + track max L-sum on the left, max M-sum on the right

# Pattern:
def max_sum_two(nums: list[int], L: int, M: int) -> int:
    pass

# Time:  O(?)
# Space: O(?)

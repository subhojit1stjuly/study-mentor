# Exercise 16 — Pattern Recognition Test
# ============================================================
# 10 problems. No hints. No pattern names given.
# For each problem:
#   1. Identify the pattern (write it as a comment)
#   2. Implement the solution
#   3. State Time and Space complexity
#
# You have learned: Hash Map, Two Pointers, Sliding Window,
# Prefix/Suffix, Kadane's, Stack, Floyd's Cycle,
# Binary Search, Queue (two stacks), Prefix Sum + Hash Map
# ============================================================


# ── Problem 1 ────────────────────────────────────────────────
# Given two strings s and t, return True if t is an anagram of s.
# An anagram uses the same characters the same number of times.
#
# is_anagram("anagram", "nagaram") → True
# is_anagram("rat", "car")        → False
# is_anagram("ab", "a")           → False

# Pattern: HashMap
def is_anagram(s: str, t: str) -> bool:
    countS,countT = {},{}
    if(len(s) != len(t)):
        return False
    for i in range(len(s)):
        countS[s[i]] = countS.get(s[i],0) + 1
        countT[t[i]] = countT.get(t[i],0) + 1
    if(countT == countS):
        return True
    else:
        return False

# Time:  O(n)
# Space: O(n)


# ── Problem 2 ────────────────────────────────────────────────
# Given an integer array sorted in non-decreasing order,
# return an array of the squares of each number,
# also in non-decreasing order.
#
# sorted_squares([-4,-1,0,3,10]) → [0,1,9,16,100]
# sorted_squares([-7,-3,2,3,11]) → [4,9,9,49,121]

# Pattern: Two pointer
def sorted_squares(nums: list[int]) -> list[int]:
    left, right = 0, len(nums)-1
    while left < right:
        sql = nums[left] * nums[left]
        sqr = nums[right] * nums[right]
        if sql > sqr:
            nums[left],nums[right] = nums[right],sql
        else:
            nums[right] = sqr
        right -=1
    if left == 0:
        nums[left] = nums[left] * nums[left]
    return nums

# Time:  O(n)
# Space: O(1)


# ── Problem 3 ────────────────────────────────────────────────
# Given an array of positive integers and a target,
# find the minimum length subarray whose sum >= target.
# Return 0 if no such subarray exists.
#
# min_subarray_len(7, [2,3,1,2,4,3]) → 2  (subarray [4,3])
# min_subarray_len(4, [1,4,4])       → 1  (subarray [4])
# min_subarray_len(11, [1,1,1,1,1])  → 0

# Pattern: sliding window
def min_subarray_len(target: int, nums: list[int]) -> int:
    window_sum,left = 0,0
    min_len = float('inf')
    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum >= target:
            min_len = min(min_len,right - left + 1)
            window_sum -= nums[left]
            left += 1
    return 0 if min_len == float('inf') else min_len

# Time:  O(?)
# Space: O(?)


# ── Problem 4 ────────────────────────────────────────────────
# Given an array, return the pivot index — the index where
# the sum of all numbers to the left equals the sum to the right.
# Return -1 if no such index exists.
# (Elements at the pivot index are NOT included in either side)
#
# pivot_index([1,7,3,6,5,6]) → 3   left=[1,7,3]=11, right=[5,6]=11
# pivot_index([1,2,3])       → -1
# pivot_index([2,1,-1])      → 0   left=[], right=[1,-1]=0

# Pattern:
def pivot_index(nums: list[int]) -> int:
    pass

# Time:  O(?)
# Space: O(?)


# ── Problem 5 ────────────────────────────────────────────────
# Given an integer array, find the contiguous subarray
# with the largest PRODUCT (not sum). Return the product.
#
# max_product([2,3,-2,4])    → 6   (subarray [2,3])
# max_product([-2,0,-1])     → 0
# max_product([-2,3,-4])     → 24  (entire array: -2*3*-4=24)
#
# Hint: Think Kadane's — but products behave differently than sums.
#       A negative * negative = positive. Track both max and min.

# Pattern:
def max_product(nums: list[int]) -> int:
    pass

# Time:  O(?)
# Space: O(?)


# ── Problem 6 ────────────────────────────────────────────────
# Baseball game scoring:
# You get a list of operations and start with an empty record.
#   - Integer "x"  → add score x
#   - "+"          → add sum of last two scores
#   - "D"          → add double of last score
#   - "C"          → remove (invalidate) last score
# Return the total sum of all scores.
#
# baseball(["5","2","C","D","+"]) → 30
#   5 → [5]
#   2 → [5,2]
#   C → [5]
#   D → [5,10]
#   + → [5,10,15]
#   sum = 30
#
# baseball(["5","-2","4","C","D","9","+","+"]) → 27

# Pattern:
def baseball(ops: list[str]) -> int:
    pass

# Time:  O(?)
# Space: O(?)


# ── Problem 7 ────────────────────────────────────────────────
# A number is "happy" if: repeatedly replacing it with the
# sum of squares of its digits eventually reaches 1.
# If it loops forever without reaching 1, it is not happy.
# Return True if n is a happy number.
#
# is_happy(19) → True   (19→82→68→100→1)
# is_happy(2)  → False  (2→4→16→37→58→89→145→42→20→4→ cycle)
#
# Hint: Think about what "loops forever" means structurally.

# Pattern:
def is_happy(n: int) -> bool:
    pass

# Time:  O(?)
# Space: O(?)


# ── Problem 8 ────────────────────────────────────────────────
# A peak element is one that is strictly greater than its neighbors.
# Given an integer array, return the index of any peak element.
# Assume nums[-1] = nums[n] = -infinity (boundaries are valleys).
#
# find_peak([1,2,3,1])     → 2
# find_peak([1,2,1,3,5,6,4]) → 1 or 5  (either valid)

# Pattern:
def find_peak(nums: list[int]) -> int:
    pass

# Time:  O(?)
# Space: O(?)


# ── Problem 9 ────────────────────────────────────────────────
# Design a class RecentCounter that counts recent requests.
# ping(t) adds a new request at time t (milliseconds) and
# returns the number of requests in the last 3000ms inclusive.
# (i.e., in the range [t-3000, t])
# All calls to ping have increasing t.
#
# rc = RecentCounter()
# rc.ping(1)    → 1   (requests: [1])
# rc.ping(100)  → 2   (requests: [1, 100])
# rc.ping(3001) → 3   (requests: [1, 100, 3001])
# rc.ping(3002) → 3   (requests: [100, 3001, 3002], 1 is out of range)

# Pattern:
from collections import deque

class RecentCounter:
    def __init__(self):
        pass

    def ping(self, t: int) -> int:
        pass


# ── Problem 10 ───────────────────────────────────────────────
# Given a binary array (only 0s and 1s), find the maximum length
# subarray with an equal number of 0s and 1s.
#
# max_equal([0,1])         → 2
# max_equal([0,1,0])       → 2
# max_equal([0,1,1,0,1,1]) → 4  (indices 0-3: [0,1,1,0])
#
# Hint: Replace each 0 with -1. Then the problem becomes:
#       "find longest subarray with sum = 0"

# Pattern:
def max_equal(nums: list[int]) -> int:
    pass

# Time:  O(?)
# Space: O(?)

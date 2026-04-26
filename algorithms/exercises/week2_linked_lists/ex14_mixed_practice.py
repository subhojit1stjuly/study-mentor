# Exercise 14 — Mixed Practice (No Hints)
# ============================================================
# These problems cover everything from Week 1 & 2.
# NO hints this time — you pick the pattern and implement.
#
# For each problem:
#   1. Write which PATTERN you're using in a comment
#   2. Implement the solution
#   3. Add Time and Space complexity
# ============================================================


# ── Problem 1 — Two Sum II (sorted input) ────────────────────
# Given a SORTED array and a target, return the 1-based indices
# of the two numbers that add up to target.
# Exactly one solution exists.
#
# two_sum_sorted([2,7,11,15], 9)  → [1, 2]
# two_sum_sorted([2,7,11,15], 18) → [2, 3]
# two_sum_sorted([2,7,11,15,21], 22) → [2, 4]
# two_sum_sorted([2,3,4], 6)      → [1, 3]
# two_sum_sorted([-1,0], -1)      → [1, 2]

# Pattern: Sliding Window.
def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) -1
    while left < right:
        two_sum = (numbers[left] + numbers[right])
        if two_sum == target:
            return (left+1,right+1)
        if two_sum > target:
            right -= 1
        else:
            left += 1
    return -1
 
# Time:  O(n)
# Space: O(1)


# ── Problem 2 — Min Stack ─────────────────────────────────────
# Design a stack that supports push, pop, top, and
# retrieving the minimum element — all in O(1).
#
# s = MinStack()
# s.push(5); s.push(3); s.push(7); s.push(2)
# s.get_min() → 2
# s.pop()
# s.get_min() → 3
# s.top()     → 7

# Pattern:
class MinStack:
    def __init__(self):
        self.stack1: list[int] = []
        self.stack2: list[int] = []

    def push(self, val: int) -> None:
        self.stack1.append(val)
        if not self.stack2:
            self.stack2.append(val)
        else:
            min_stack = min(self.stack2[-1],val)
            self.stack2.append(min_stack)

    def pop(self) -> None:
        if self.stack1:
            self.stack1.pop()
            self.stack2.pop()

    def top(self) -> int:
        if self.stack1:
            return self.stack1[-1]
        else:
            return -1

    def get_min(self) -> int:
        if self.stack1:
            return self.stack2[-1]    
# push/pop/top/get_min Time: O(1)
# Space: O(1)


# ── Problem 3 — Longest Repeating Character Replacement ──────
# Given a string and integer k, you can replace at most k
# characters. Return the length of the longest substring
# containing the same letter after replacements.
#
# char_replacement("ABAB", 2)   → 4  (replace both B's → "AAAA")
# char_replacement("AABABBA", 1) → 4  (replace one B → "AABAAAA" window)
#
# Hint: sliding window
#       window is valid if: (window_size - max_freq_in_window) <= k

# Pattern: Sliding Window with hashMaps
def char_replacement(s: str, k: int) -> int:
    left,window_size,max_freq = 0,0,0
    freq = {}
    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1
        max_freq = max(max_freq,freq[s[right]])
        if (right - left + 1) - max_freq > k:
            freq[s[left]] -= 1
            left += 1
        window_size = max(window_size, right - left + 1)
    return window_size



# Time:  O(?)
# Space: O(?)


# ── Problem 4 — Find Duplicate Number ────────────────────────
# Given an array of n+1 integers where each integer is in [1,n],
# there is exactly one duplicate. Find it.
# You must NOT modify the array. Use O(1) extra space.
#
# find_duplicate([1,3,4,2,2]) → 2
# find_duplicate([3,1,3,4,2]) → 3
# find_duplicate([3,1,4,2,3]) → 3
# find_duplicate([2,5,9,6,9,3,8,9,7,1]) → 9
#
# Hint: treat array values as "next pointers" — like a linked
#       list with a cycle. Use slow/fast pointer (Floyd's).
#       The duplicate is the cycle entry point.

# Pattern: two Pointer(slow and fast pointer)
# Phase 1
# slow = 2, fast = 2,
# slow = 9, fast = 1,
# slow = 1, fast = 3,
# slow = 5, fast = 8,
# slow = 3, fast = 9,
# slow = 6, fast = 5,
# slow = 8, fast = 6,
# slow = 7, fast = 7,
# Phase 2
# slow = 2, fast = 7,
# slow = 9, fast = 9,

def find_duplicate(nums: list[int]) -> int:
    slow = nums[0]
    fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

# Time:  O(n)
# Space: O(1)


# ── Problem 5 — Search a 2D Matrix ───────────────────────────
# Given an m×n matrix where:
#   - rows are sorted left to right
#   - first integer of each row > last integer of previous row
# Return True if target exists in the matrix.
#
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# search_matrix(matrix, 3)  → True
# search_matrix(matrix, 13) → False
#
# Hint: treat the matrix as a flat sorted array of m*n elements.
#       Use binary search. Convert mid index to row/col:
#       row = mid // cols,  col = mid % cols

# Pattern:
def search_matrix(matrix: list[list[int]], target: int) -> bool:
    pass

# Time:  O(?)
# Space: O(?)

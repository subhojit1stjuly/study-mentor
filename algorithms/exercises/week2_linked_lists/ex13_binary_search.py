# Exercise 13 — Binary Search
# ============================================================
# TASK: Implement each function using binary search.
#
# RULES:
#   - Every solution must be O(log n) — no linear scans
#   - Use the template: left, right, mid, while left <= right
#   - Add Time and Space complexity for each
#
# TEMPLATE REMINDER:
#   left, right = 0, len(nums) - 1
#   while left <= right:
#       mid = left + (right - left) // 2
#       if nums[mid] == target: ...
#       elif nums[mid] < target: left = mid + 1
#       else: right = mid - 1
#   return -1
# ============================================================


# ── Problem 1 — Classic Binary Search ────────────────────────
# Return the index of target in nums, or -1 if not found.
# nums is sorted in ascending order.
#
# search([1,3,5,7,9,11], 7)  → 3
# search([1,3,5,7,9,11], 6)  → -1
# search([5], 5)              → 0
# search([], 1)               → -1

def search(nums: list[int], target: int) -> int:
    left,right = 0,len(nums)-1
    while left <= right:
        mid = left + (right-left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
             right = mid -1 
    return -1
# Time:  O(logn)
# Space: O(1)


# ── Problem 2 — First Bad Version ────────────────────────────
# You have n versions [1, 2, ..., n]. At some point a bad
# version was introduced and ALL versions after it are also bad.
# is_bad(version) returns True if that version is bad.
# Find the FIRST bad version using minimum calls to is_bad.
#
# n=5, first_bad=4 → is_bad: [F,F,F,T,T] → return 4
# n=1, first_bad=1 → return 1
#
# Hint: binary search on the version numbers 1..n
#       if mid is bad → answer is mid or earlier → right = mid
#       if mid is good → answer is after mid → left = mid + 1
# is_bad = [F,F,F,T,T]

def first_bad_version(n: int, is_bad: callable) -> int:
    left,right = 1,n
    while left < right:
        mid = left + (right - left) // 2
        if is_bad(mid):
            right = mid
        else:
            left = mid + 1
    return left
# Time:  O(logn)
# Space: O(1)


# ── Problem 3 — Search in Rotated Sorted Array ───────────────
# A sorted array was rotated at some unknown pivot.
# e.g. [0,1,2,4,5,6,7] → rotated → [4,5,6,7,0,1,2]
# Find the index of target, or -1 if not found.
#
# search_rotated([4,5,6,7,0,1,2], 0) → 4
# search_rotated([6,7,1,2,3,4,5], 3) → 4
# search_rotated([1], 0)              → -1
#
# Hint: one half is ALWAYS sorted after any rotation.
#       Check which half is sorted, then decide which half
#       the target could be in.
#       if nums[left] <= nums[mid]: left half is sorted
#       else: right half is sorted

def search_rotated(nums: list[int], target: int) -> int:
    left,right = 0, len(nums)-1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[left] <= nums[mid]:
            if nums[left] <= target and nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[right] >= target and nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    return -1

# Time:  O(?)
# Space: O(?)


# ── Problem 4 — Find Minimum in Rotated Sorted Array ─────────
# Given a rotated sorted array, find the minimum element.
#
# find_min([3,4,5,1,2])   → 1
# find_min([4,5,6,7,0,1,2]) → 0
# find_min([11,13,15,17])  → 11  (not rotated)
#
# Hint: the minimum is the only element smaller than its
#       left neighbor (the rotation point).
#       if nums[mid] > nums[right]: min is in right half
#       else: min is in left half (including mid)

def find_min(nums: list[int]) -> int:
    pass

# Time:  O(?)
# Space: O(?)

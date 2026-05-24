# Exercise 15 — Random Pattern Drill
# ============================================================
# No pattern names given. No hints.
# You must:
#   1. Identify the pattern
#   2. Implement the solution
#   3. Add Time and Space complexity
#
# Difficulty: Easy to Medium
# ============================================================


# ── Problem 1 ────────────────────────────────────────────────
# Given an array of integers, return True if any value
# appears at least twice. Return False if all elements distinct.
#
# contains_duplicate([1,2,3,1])     → True
# contains_duplicate([1,2,3,4])     → False
# contains_duplicate([1,1,1,3,3,4]) → True

# Pattern: hasmap memory
def contains_duplicate(nums: list[int]) -> bool:
   seen = {}
   for i in range(len(nums)):
       if nums[i] in seen:
           return True
       seen[nums[i]] = i
   return False

# Time:  O(n)
# Space: O(n)


# ── Problem 2 ────────────────────────────────────────────────
# Given a string, return True if it is a palindrome,
# considering only alphanumeric characters, ignoring case.
#
# is_palindrome("A man, a plan, a canal: Panama") → True
# is_palindrome("race a car")                     → False
# is_palindrome(" ")                              → True

# Pattern: Two Pointers, Strings
def is_palindrome(s: str) -> bool:
    left , right = 0 , len(s) - 1
    while left < right:
        while not s[left].isalnum():
            left += 1
        while not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
# Time:  O(n)
# Space: O(1)


# ── Problem 3 ────────────────────────────────────────────────
# Given an integer array, move all zeroes to the end
# while maintaining relative order of non-zero elements.
# Do it IN-PLACE.
#
# move_zeroes([0,1,0,3,12]) → [1,3,12,0,0]
# move_zeroes([0,0,1])      → [1,0,0]
# move_zeroes([1,2,3])      → [1,2,3]

# Pattern: slow and fast pointer
def move_zeroes(nums: list[int]) -> list:
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left],nums[right] = nums[right], nums[left]
            left += 1
    return nums
# Time:  O(n)
# Space: O(1)


# ── Problem 4 ────────────────────────────────────────────────
# Given a sorted array, remove duplicates in-place.
# Return the count of unique elements.
# (The first k elements of the array should be the unique values)
#
# remove_duplicates([1,1,2])          → 2  (array becomes [1,2,...])
# remove_duplicates([0,0,1,1,1,2,2,3]) → 4  (array becomes [0,1,2,3,...])

# Pattern: two pointer
def remove_duplicates(nums: list[int]) -> int:
    left  = 1
    for right in range(1,len(nums)):
        if nums[right] != nums[right - 1]:
            left += 1
    return left
# Time:  O(n)
# Space: O(1)


# ── Problem 5 ────────────────────────────────────────────────
# Given a string s, find the length of the longest
# substring without repeating characters.
#
# length_of_longest("abcabcbb") → 3  ("abc")
# length_of_longest("bbbbb")   → 1  ("b")
# length_of_longest("pwwkew")  → 3  ("wke")
# length_of_longest("")        → 0

# Pattern:sliding window
def length_of_longest(s: str) -> int:
    left , window_size = 0,0
    seen = {}
    for right in range(len(s)):
        while s[right] in seen:
            seen.pop(s[left])
            left += 1
        seen[s[right]] = 1
        window_size = max(window_size, right - left + 1)
    return window_size
# Time:  O(n)
# Space: O(n)


# ── Problem 6 ────────────────────────────────────────────────
# Given an array of integers and a target sum,
# return the count of subarrays that sum to target.
#
# subarray_sum([1,1,1], 2)       → 2
# subarray_sum([1,2,3], 3)       → 2
# subarray_sum([1,-1,1,1], 2)    → 2
#
# Hint: prefix sum + hash map
#       count[prefix] = how many times this prefix sum was seen
#       if (current_prefix - target) was seen before → found a subarray

# Pattern:
def subarray_sum(nums: list[int], target: int) -> int:
    seen = {0:1}
    prefix = 0
    count = 0
    for i in range(len(nums)):
        prefix += nums[i]
        if (prefix - target) in seen:
            count += seen[prefix-target]
        seen[prefix] = seen.get(prefix,0) + 1
    return count

# Time:  O(?)
# Space: O(?)


# ── Problem 7 ────────────────────────────────────────────────
# Given a sorted array and a target, return the index where
# target should be inserted to keep the array sorted.
# If target exists, return its index.
#
# search_insert([1,3,5,6], 5) → 2
# search_insert([1,3,5,6], 2) → 1
# search_insert([1,3,5,6], 7) → 4
# search_insert([1,3,5,6], 0) → 0

# Pattern:
def search_insert(nums: list[int], target: int) -> int:
    left,right = 0, len(nums) - 1
    while left<=right:
        mid = left + (right - left) // 2 
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left
# Time:  O(log n )
# Space: O(1)

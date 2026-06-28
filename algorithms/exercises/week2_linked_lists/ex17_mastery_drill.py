# Exercise 17 — Pattern Mastery Drill
# ============================================================
# 10 new problems. Identify the pattern and solve.
# Goal: Build confidence through repetition.
#
# Your 10 patterns: Hash Map, Two Pointers, Sliding Window,
# Prefix/Suffix, Kadane's, Stack, Floyd's Cycle,
# Binary Search, Queue, Prefix Sum + Hash Map
# ============================================================


# ── Problem 1 ────────────────────────────────────────────────
# LeetCode 1: https://leetcode.com/problems/two-sum/
#
# Given an array of integers, find two numbers that add up to a
# specific target. Return their indices.
# Assume exactly one solution exists, and you cannot use the same
# element twice.
#
# two_sum([2,7,11,15], 9)  → [0,1]  (2+7=9)
# two_sum([3,2,4], 6)      → [1,2]  (2+4=6)
# two_sum([3,3], 6)        → [0,1]  (3+3=6)

# Pattern: hashMap
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i,num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement],i]
        seen[num] = i
    return []

# Time:  O(n)
# Space: O(n)


# ── Problem 2 ────────────────────────────────────────────────
# LeetCode 345: https://leetcode.com/problems/reverse-vowels-of-a-string/
#
# Given a string, reverse only the vowels in it.
# Vowels are 'a', 'e', 'i', 'o', 'u' (both cases).
#
# reverse_vowels("hello")     → "holle"
# reverse_vowels("leetcode")  → "leotcede"
# reverse_vowels("aA")        → "Aa"

# Pattern: two pointer
def reverse_vowels(s: str) -> str:
    vowelSet = set('aAeEiIoOuU')
    left, right = 0, len(s) - 1
    resultString = list(s)
    while left < right:
        if resultString[left] not in vowelSet:
            left += 1
        elif resultString[right] not in vowelSet:
            right -= 1
        else:
            resultString[left],resultString[right] = resultString[right],resultString[left]
            right -= 1
            left += 1
    return "".join(resultString)

# Time:  O(n)
# Space: O(n) for list conversion


# ── Problem 3 ────────────────────────────────────────────────
# LeetCode 340: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
#
# Given a string, find the length of the longest substring with
# at most K distinct characters.
#
# longest_k_distinct("eceba", k=2)    → 3  ("ece")
# longest_k_distinct("aa", k=1)       → 2  ("aa")
# longest_k_distinct("abcabc", k=3)   → 6  ("abcabc")

# Pattern: sliding window (variable length)
def longest_k_distinct(s: str, k: int) -> int:
    left,max_len = 0,0
    window = {}
    for right in range(len(s)):
        # expand the window
        window[s[right]] = window.get(s[right],0) + 1
        # validate if teh window is valid or not
        while len(window) > k and left < right:
            if window[s[left]] > 1:
                window[s[left]] -= 1
            else:
                window.pop(s[left])
            left += 1
        max_len = max(max_len,right - left + 1)
    return max_len


          
# Time:  O(n)
# Space: O(k)


# ── Problem 4 ────────────────────────────────────────────────
# LeetCode 238: https://leetcode.com/problems/product-of-array-except-self/
#
# Given an array, return a new array where each element
# is the product of all numbers in the original array
# except the one at that index.
# Do NOT use division.
#
# product_except_self([1,2,3,4])  → [24,12,8,6]
# product_except_self([2,3,4,5])  → [60,40,30,24]
# product_except_self([-1,1,0,-3,3]) → [0,0,9,0,0]

# Pattern: prefix and suffix
def product_except_self(nums: list[int]) -> list[int]:
    result = [1] * len(nums)
    for i in range(1,len(nums)):
        result[i] = result[i-1] * nums[i-1]
    right = 1
    for i in range(len(nums)-1,-1,-1):
        result[i] *= right
        right *= nums[i]
    return result

# Time:  O(n)
# Space: O(1) without the result array


# ── Problem 5 ────────────────────────────────────────────────
# LeetCode 674: https://leetcode.com/problems/longest-continuous-increasing-subsequence/
#
# Given an integer array, return the length of the longest
# strictly increasing subarray.
#
# longest_increasing([1,3,5,4,7])  → 3  ([1,3,5])
# longest_increasing([2,2,2,2])    → 1
# longest_increasing([5,4,3,2,1])  → 1

# Pattern: sliding window with variable size
def longest_increasing(nums: list[int]) -> int:
    left = 0
    max_len = 0
    best = nums[0]
    for right in range(len(nums)):
        # if the window is in-valid
        if best+1 > nums[right]:
            left = right
        best = nums[right]
        max_len = max(max_len, right - left + 1)
    return max_len

# Time:  O(?)
# Space: O(?)


# ── Problem 6 ────────────────────────────────────────────────
# LeetCode 20: https://leetcode.com/problems/valid-parentheses/
#
# Given a string with just '(', ')', '{', '}', '[', ']',
# determine if it is valid.
# Open brackets must be closed by the same type in correct order.
#
# is_valid("()")       → True
# is_valid("()[]{}")   → True
# is_valid("(]")       → False
# is_valid("([)]")     → False
# is_valid("{[]}")     → True
# is_valid("{[{[()]}]}")     → True

# Pattern: stack 
def is_valid(s: str) -> bool:
    valide_parenthesis = { ')':'(', '}':'{', ']':'['}
    stack = []
    for i,char in enumerate(s):
        if not stack and char in valide_parenthesis:
            return False
        if char in valide_parenthesis and stack[-1] == valide_parenthesis.get(char):
            stack.pop()
        else:
            stack.append(char)
    return not stack

# Time:  O(n)
# Space: O(1)


# ── Problem 7 ────────────────────────────────────────────────
# LeetCode 141: https://leetcode.com/problems/linked-list-cycle/
#
# Given a linked list, detect if there is a cycle.
# A cycle exists if you can reach the same node again
# by continuously following the `next` pointer.
#
# Return True if cycle exists, False otherwise.
# pattern - floyed cycle detection
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Pattern:
def has_cycle(head: ListNode) -> bool:
    slow,fast = head,head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Time:  O(logn)
# Space: O(1)


# ── Problem 8 ────────────────────────────────────────────────
# LeetCode 121: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#
# You are given an array representing stock prices on different days.
# Find the maximum profit you can achieve by buying and selling once.
# You must buy before you sell.
#
# max_profit([7,1,5,3,6,4])  → 5  (buy at 1, sell at 6)
# max_profit([7,6,4,3,1])    → 0  (no profit possible)
# max_profit([2,4,1])        → 2  (buy at 2, sell at 4)

# Pattern: dynamic programming problem
def max_profit(prices: list[int]) -> int:
    profit = 0
    left = 0
    for right in range(1,len(prices)):
        profit = max(profit,prices[right] - prices[left])
        while prices[left] > prices[right]:
            left += 1
    return profit

# Time:  O(n)
# Space: O(1)


# ── Problem 9 ────────────────────────────────────────────────
# LeetCode 153: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#
# Given a sorted array rotated at some unknown pivot,
# find the index of the minimum element.
# (Array was originally sorted in ascending order, then rotated)
#
# find_min_index([3,4,5,1,2])      → 3
# find_min_index([4,5,6,7,0,1,2])  → 4
# find_min_index([1,2,3,4,5])      → 0  (not rotated)

# Pattern: binary search
# here we are comparing with right because if the array is [1,2,3,4,5,6]
# then while compring with left will discard the smallest element.
# soif we are told to get the heighest element then we should compare with right.
def find_min_index(nums: list[int]) -> int:
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + (right -left) // 2
        if nums[mid] > nums[right]:
           left = mid + 1
        else:
            right = mid
    return left
def find_max_index(nums: list[int]) -> int:
    left = 0
    right = len(nums) - 1
    while left< right:
        mid = left + (right - left) // 2
        if nums[mid] >= nums[left]:
            left = mid 
        else:
            right = mid - 1
    return left

# Time:  O(log n)
# Space: O(1)


# ── Problem 10 ───────────────────────────────────────────────
# LeetCode 560: https://leetcode.com/problems/subarray-sum-equals-k/
#
# Given an array, find the number of subarrays that sum
# to exactly 0.
#
# count_zero_sum([0,0,0])      → 6  ([0],[0],[0],[0,0],[0,0],[0,0,0])
# count_zero_sum([1,-1,0])     → 3  ([-1,1], [0], [1,-1,0])
# count_zero_sum([1,2,3])      → 0

# prefix_sum - left_sum = k
# prefix_sum - k = left_sum
# Pattern: prefix sum + HashMap
def count_zero_sum(nums: list[int]) -> int:
    seen = {0:1}
    count = 0
    prefix_sum = 0
    target = 0
    for i,num in enumerate(nums):
        prefix_sum += num
        look_for = prefix_sum - target
        if look_for in seen:
            count += seen.get(look_for,0)
        seen[prefix_sum] = seen.get(prefix_sum,0) + 1
    return count
        


# Time:  O(n)
# Space: O(1)

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
    result = [0] * len(nums)
    pos = len(nums) - 1
    while left <= right:
        sql = nums[left] ** 2
        sqr = nums[right] ** 2
        if sql > sqr:
            result[pos] = sql
            left += 1
        else:
            result[pos] = sqr
            right -= 1
        pos -=1
    return result

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
    total = 0
    left_sum,right_sum = 0,0
    for i in range(len(nums)):
        total += nums[i]
    for i in range(len(nums)):
        right_sum = total - left_sum - nums[i]
        if right_sum == left_sum:
            return i
        else:
            left_sum += nums[i]
    return -1

# Time:  O(n)
# Space: O(1)


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

# Pattern: Kadane's
def max_product(nums: list[int]) -> int:
    result = max_product = nums[0]
    min_product = nums[0]
    for i in range(nums[1:]):
        candidates = (nums[i],max_product*nums[i],min_product*nums[i])
        max_product = max(candidates)
        min_product = min(candidates)
        result = max(result,candidates)
    return result
# Time:  O(n)
# Space: O(1)
# reasoning behind the logic : - 
# there are three candidates -
# why nums[i] is a candidate ? since it is a contiguous subarray, 
# means if we would have made th result as a candidate, then we would have carring the maxvalue which is wrong 
# because we are not calculating the max posetive product.
# why max_product * nums[i] is a candidate ? - becasue it stores the max value in the contigues sub arrays
# why min_product * nums[i] is a candidate ? becasue it stores the min value in the contigues sub array, since two negetive value 
# can be multiplied and gives us the greater number. 
# now why result is calculated with max between result and candidtes?
# since a single item in the array can be max , result it self can be max.
# so we used the max_product and min_product as a memory because two negetive numbers can give us a higher posetive number.


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


# reasoning behind the logic : - 
# Question to ask ? 
# * what if the array starts with + or D, or C
# * what if the + appears as the first / second Element in the array ?
# Constraints -
# * every number is a integer, not a float 
# * there can be negetive numbers as a score,
# * there can never be any other extra charector in the list other than these C, D, +
# analogy - 
# since the items in the list is charectors, we need to make sure to convert them to integer or atleast check in every way.
# so my first naive strategie will be to besically use a extra list for keeping the track
# afterwards I will think about more storage optimised way to solve.


# Pattern: stack
def baseball(ops: list[str]) -> int:
    final_scores = []
    for i in range(len(ops)):
        if ops[i] == '+':
            if final_scores and len(final_scores)>=2:
                final_scores.append(final_scores[-1] + final_scores[-2])
        elif ops[i] == 'C':
            if final_scores:
                final_scores.pop()
        elif ops[i] == 'D':
            final_scores.append(final_scores[-1] * 2)
        else:
            final_scores.append(int(ops[i]))
    result = 0
    for i in range(len(final_scores)):
        result += final_scores[i]
    return result

# Time:  O(n+n)
# Space: O(n)


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

# reasoning behind the logic : - 
# the number can be only posetive right,and there are no flaoting points ?
# so there is a repetative function that calculates 
# the sum of squares of its digits, which can be converted into 
# a recursive method which eventually return true if the number is 1, 
# but since the calculation can be looped forever, so we need to 
# make sure to break it if there are any loops. so in order to
# find if there are any loops, we can just check that 
# the sum of squares of its digits of current number == 
# the sum of squares of its digits of actual number. but here the problem is 
# that we can not remember the original number when the loop become infinite. so
# first will try to solve this using simple loop. correct me if i am wrong 
# or if there are better approaches.
# final undestanding is that, i can create helper methods to solve a problem.

# Pattern: Floyd's cycle detection
def is_happy(n: int) -> bool:
    slow, fast = n,n
    while fast != 1:
        fast = digits_square(fast)
        fast = digits_square(fast)
        slow= digits_square(slow)
        if slow == fast:
            break

    return fast == 1
def digits_square(num:int)->int:
    total = 0
    while num != 0:
            total += (num % 10) ** 2
            num = num // 10
    return total 

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

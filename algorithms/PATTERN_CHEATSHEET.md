# DSA Pattern Cheat Sheet

Quick reference for the 10 core patterns learned so far.

---

## 1. Hash Map

**When to use:**
- Need O(1) lookup for existence/counting
- Finding pairs/complements (Two Sum)
- Counting frequency of elements
- Detecting duplicates

**Key indicators:**
- "find two numbers that..."
- "check if contains..."
- "count occurrences..."
- "first unique/duplicate..."

**Template:**
```python
seen = {}
for item in arr:
    if item in seen:
        # found
    seen[item] = value  # or seen[item] = seen.get(item, 0) + 1
```

**Complexity:** Time O(n), Space O(n)

**Example problems:** Two Sum, Valid Anagram, Contains Duplicate

---

## 2. Two Pointers

**When to use:**
- Sorted array or string
- Finding pairs with a condition
- In-place array manipulation
- Reversing, removing elements

**Key indicators:**
- Array is sorted
- "two numbers that sum to..."
- "remove duplicates in-place..."
- "reverse..."

**Template:**
```python
left, right = 0, len(arr) - 1
while left < right:
    if condition:
        left += 1
    else:
        right -= 1
```

**Complexity:** Time O(n), Space O(1)

**Example problems:** Two Sum II, Valid Palindrome, Container With Most Water, Reverse Vowels

---

## 3. Sliding Window

**When to use:**
- Subarray/substring problems with positive integers
- "Longest/shortest subarray with..."
- "Maximum sum of subarray size k"
- Window size can be fixed or variable

**Key indicators:**
- "substring with..."
- "minimum/maximum length subarray..."
- "at most K distinct..."
- All elements are positive

**Template (variable size):**
```python
left = 0
for right in range(len(arr)):
    # expand window
    window_data[arr[right]] += 1
    
    while window_invalid:
        # shrink window
        window_data[arr[left]] -= 1
        left += 1
    
    # update answer
    max_len = max(max_len, right - left + 1)
```

**Template (fixed size):**
```python
for i in range(len(arr)):
    window_sum += arr[i]
    if i >= k - 1:
        max_sum = max(max_sum, window_sum)
        window_sum -= arr[i - k + 1]
```

**Complexity:** Time O(n), Space O(1) to O(k)

**Example problems:** Longest Substring Without Repeating, Min Subarray Len, Max Sum of K elements

---

## 4. Prefix/Suffix

**When to use:**
- Need product/sum of everything except current index
- Left-to-right + right-to-left passes
- Cannot use division

**Key indicators:**
- "product/sum of all except self"
- "left array and right array"

**Template:**
```python
# Two passes
result = [1] * n
# Pass 1: left products
for i in range(1, n):
    result[i] = result[i-1] * nums[i-1]
# Pass 2: right products
right = 1
for i in range(n-1, -1, -1):
    result[i] *= right
    right *= nums[i]
```

**Complexity:** Time O(n), Space O(1) excluding output

**Example problems:** Product of Array Except Self

---

## 5. Kadane's Algorithm

**When to use:**
- Maximum/minimum subarray sum or product
- Contiguous subarray optimization

**Key indicators:**
- "maximum sum subarray"
- "contiguous elements"

**Template (sum):**
```python
curr = best = nums[0]
for num in nums[1:]:
    curr = max(num, curr + num)  # restart or extend
    best = max(best, curr)
return best
```

**Template (product):**
```python
curr_max = curr_min = best = nums[0]
for num in nums[1:]:
    candidates = (num, curr_max * num, curr_min * num)
    curr_max = max(candidates)
    curr_min = min(candidates)  # track negatives
    best = max(best, curr_max)
return best
```

**Complexity:** Time O(n), Space O(1)

**Example problems:** Maximum Subarray, Maximum Product Subarray

---

## 6. Stack

**When to use:**
- Matching pairs (parentheses, brackets)
- "Next greater/smaller element"
- Nested structures
- Undo/redo operations

**Key indicators:**
- "valid parentheses"
- "next greater..."
- "daily temperatures"
- Last-in-first-out behavior

**Template:**
```python
stack = []
for item in items:
    if condition:
        stack.append(item)
    else:
        stack.pop()
```

**Monotonic Stack:**
```python
stack = []  # stores indices
for i, val in enumerate(nums):
    while stack and nums[stack[-1]] < val:
        idx = stack.pop()
        result[idx] = i - idx  # distance
    stack.append(i)
```

**Complexity:** Time O(n), Space O(n)

**Example problems:** Valid Parentheses, Daily Temperatures, Baseball Game, MinStack

---

## 7. Floyd's Cycle Detection

**When to use:**
- Detect cycle in linked list
- Find duplicate in array (treating values as pointers)
- Space O(1) required

**Key indicators:**
- "detect cycle"
- "find duplicate" (with O(1) space constraint)
- "linked list" + "cycle"

**Template:**
```python
slow, fast = head, head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True  # cycle detected
return False
```

**Find duplicate in array:**
```python
slow, fast = nums[0], nums[0]
# Phase 1: detect cycle
while True:
    slow = nums[slow]
    fast = nums[nums[fast]]
    if slow == fast:
        break
# Phase 2: find entrance
slow = nums[0]
while slow != fast:
    slow = nums[slow]
    fast = nums[fast]
return slow
```

**Complexity:** Time O(n), Space O(1)

**Example problems:** Linked List Cycle, Happy Number, Find Duplicate Number

---

## 8. Binary Search

**When to use:**
- Sorted array
- Search space can be halved
- Finding target or insertion point
- Answer-space search (find minimum/maximum that satisfies condition)

**Key indicators:**
- Array is sorted
- "find target in O(log n)"
- "rotated sorted array"
- "find minimum/maximum that..."

**Template (classic):**
```python
left, right = 0, len(arr) - 1
while left <= right:
    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
return -1
```

**Template (find boundary):**
```python
left, right = 0, len(arr) - 1
while left < right:
    mid = left + (right - left) // 2
    if condition:
        right = mid  # don't exclude mid
    else:
        left = mid + 1
return left
```

**Complexity:** Time O(log n), Space O(1)

**Example problems:** Binary Search, Search Insert Position, Find Min in Rotated Array, Find Peak Element

---

## 9. Queue (Two Stacks / Deque)

**When to use:**
- FIFO order required
- Sliding window of time/events
- Recent K elements

**Key indicators:**
- "last K requests"
- "recent N items"
- "moving average"
- Time windows

**Template (deque):**
```python
from collections import deque
q = deque()
q.append(item)       # add to right
q.popleft()          # remove from left
q[0]                 # peek left
len(q)               # size
```

**Template (two stacks):**
```python
class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    
    def enqueue(self, x):
        self.in_stack.append(x)
    
    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()
```

**Complexity:** Time O(1) amortized, Space O(n)

**Example problems:** MyQueue, Recent Counter, Moving Average

---

## 10. Prefix Sum + Hash Map

**When to use:**
- Count subarrays with exact sum
- Longest subarray with sum = X
- Can have negative numbers
- Need to check all prefix pairs

**Key indicators:**
- "count subarrays that sum to K"
- "longest subarray with sum = 0"
- "sum equals..." (exact match)
- May have negative numbers

**Template:**
```python
seen = {0: 1}  # or {0: -1} for length problems
prefix = 0
count = 0  # or max_len = 0

for i, num in enumerate(nums):
    prefix += num
    
    # For counting:
    count += seen.get(prefix - target, 0)
    seen[prefix] = seen.get(prefix, 0) + 1
    
    # For length:
    if prefix - target in seen:
        max_len = max(max_len, i - seen[prefix - target])
    if prefix not in seen:
        seen[prefix] = i

return count  # or max_len
```

**Why {0: 1} or {0: -1}?**
- `{0: 1}` for counting: "empty prefix" has sum 0, seen once
- `{0: -1}` for length: prefix 0 at "before array" position

**Complexity:** Time O(n), Space O(n)

**Example problems:** Subarray Sum Equals K, Contiguous Array (equal 0s and 1s)

---

## Pattern Decision Tree

```
Input is sorted? 
  ├─ Yes → Binary Search or Two Pointers
  └─ No  → Continue

Need O(1) lookup?
  ├─ Yes → Hash Map
  └─ No  → Continue

Subarray/substring problem?
  ├─ Positive only + shrinkable → Sliding Window
  ├─ Exact sum/count needed → Prefix Sum + Hash Map
  └─ Max/min sum/product → Kadane's

Linked list cycle?
  └─ Floyd's Cycle Detection

Matching pairs / nested structure?
  └─ Stack

FIFO / recent K items?
  └─ Queue

Left-right products/sums?
  └─ Prefix/Suffix
```

---

## Common Mistakes to Avoid

1. **Off-by-one errors:**
   - `right = len(arr)` instead of `len(arr) - 1`
   - `while left <= right` vs `while left < right`

2. **Pointer conditions:**
   - Forgetting `and left < right` in nested while loops
   - Not saving `next` pointer before relinking in linked lists

3. **Hash map edge cases:**
   - Not checking `if key in map` before accessing
   - Forgetting to initialize `{0: 1}` in prefix sum problems

4. **Sliding window:**
   - Using `seen.clear()` instead of gradual shrinking
   - Forgetting to remove `s[left]` from window when shrinking

5. **Space complexity:**
   - Auxiliary data structures (hash map, stack) are O(n), not O(1)
   - Recursion has O(depth) space for call stack

---

## Practice Strategy

1. **Pattern recognition drill:**
   - Read problem → identify pattern in 30 seconds
   - Don't code yet, just name the pattern

2. **Template recall:**
   - Can you write the template from memory?
   - Practice writing each template 3 times

3. **Variation practice:**
   - Same pattern, different problem
   - Builds confidence and speed

4. **Mixing patterns:**
   - Some problems need 2 patterns (e.g., Sliding Window + Hash Map)
   - Advanced problems combine patterns

---

## Next Steps

After mastering these 10 patterns, you're ready for:
- **Trees & BSTs** — DFS, BFS, tree traversals
- **Graphs** — DFS, BFS, topological sort, shortest path
- **Dynamic Programming** — memoization, tabulation, state transitions
- **Backtracking** — permutations, combinations, constraints
- **Greedy** — interval scheduling, activity selection

**Goal:** With these 10 patterns, you can solve 60-70% of LeetCode Easy/Medium problems.

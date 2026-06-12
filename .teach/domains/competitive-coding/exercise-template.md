# Competitive Coding - Sample Exercise Template

This is a template for creating practice exercises in the competitive coding domain.

## Problem Template

```markdown
# Exercise: [Problem Name] ([Difficulty])

**Pattern**: [Two Pointers / Sliding Window / DP / etc.]
**Topics**: [Arrays, Strings, etc.]
**Difficulty**: ⭐ Easy / ⭐⭐ Medium / ⭐⭐⭐ Hard
**Estimated Time**: [15 / 30 / 45 minutes]

## Problem Statement

[Clear, concise problem description]

## Examples

### Example 1:
**Input**: `[example input]`
**Output**: `[example output]`
**Explanation**: [Why this is the answer]

### Example 2:
**Input**: `[example input]`
**Output**: `[example output]`

## Constraints

- [Constraint 1 with range]
- [Constraint 2]
- [Important assumptions]

## Test Cases

```python
def test_solution():
    assert solution([input1]) == expected1
    assert solution([input2]) == expected2
    assert solution([edge_case]) == expected_edge
```

## Hints (Progressive)

<details>
<summary>Hint 1 (Click after 10 minutes)</summary>

[High-level approach hint]
</details>

<details>
<summary>Hint 2 (Click after 20 minutes)</summary>

[More specific guidance]
</details>

<details>
<summary>Hint 3 (Click after 30 minutes)</summary>

[Almost the solution]
</details>

## Solution

<details>
<summary>Solution (Click after attempting or 45 minutes)</summary>

```python
def solution(input):
    """
    [Brief explanation of approach]
    """
    # Your solution here
    pass
```

### Explanation

[Detailed explanation of the solution]

**Time Complexity**: O(?)
**Space Complexity**: O(?)

### Why This Works

[Intuition behind the solution]

### Common Mistakes

- ❌ [Common mistake 1]
- ❌ [Common mistake 2]

</details>

## Alternative Solutions

<details>
<summary>Alternative Approach 1</summary>

[Different way to solve, with trade-offs]
</details>

## Related Problems

- [Related Problem 1] - Similar pattern
- [Related Problem 2] - Builds on this concept

## Reflection Questions

After solving, consider:
1. What was the key insight?
2. What pattern does this problem use?
3. Could you solve a harder variant?
4. How would you explain this to someone else?

---

**Status**: [ ] Not Started | [ ] Attempted | [ ] Solved with Hints | [✓] Solved Independently
**Date Solved**: ___________
**Time Taken**: ___________ minutes
**Notes**: 
```

## Example: Two Sum Problem

# Exercise: Two Sum (Easy)

**Pattern**: Hash Map / Array
**Topics**: Arrays, Hash Tables
**Difficulty**: ⭐ Easy
**Estimated Time**: 15 minutes

## Problem Statement

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Examples

### Example 1:
**Input**: `nums = [2,7,11,15], target = 9`
**Output**: `[0,1]`
**Explanation**: Because nums[0] + nums[1] == 9, we return [0, 1].

### Example 2:
**Input**: `nums = [3,2,4], target = 6`
**Output**: `[1,2]`

### Example 3:
**Input**: `nums = [3,3], target = 6`
**Output**: `[0,1]`

## Constraints

- 2 ≤ nums.length ≤ 10⁴
- -10⁹ ≤ nums[i] ≤ 10⁹
- -10⁹ ≤ target ≤ 10⁹
- Only one valid answer exists.

## Test Cases

```python
def test_two_sum():
    assert two_sum([2,7,11,15], 9) == [0,1]
    assert two_sum([3,2,4], 6) == [1,2]
    assert two_sum([3,3], 6) == [0,1]
    assert two_sum([-1,-2,-3,-4,-5], -8) == [2,4]
```

## Hints (Progressive)

<details>
<summary>Hint 1 (Click after 10 minutes)</summary>

The brute force approach would check every pair of numbers (O(n²)). Can you do better with a data structure?
</details>

<details>
<summary>Hint 2 (Click after 15 minutes)</summary>

Use a hash map to store numbers you've seen. For each number, check if (target - number) exists in the map.
</details>

<details>
<summary>Hint 3 (Click after 20 minutes)</summary>

Iterate through the array once. For each number `num`, check if `target - num` is in your hash map. If yes, return the indices. If not, add `num` and its index to the map.
</details>

## Solution

<details>
<summary>Solution (Click after attempting)</summary>

```python
def two_sum(nums, target):
    """
    Use hash map to find complement in O(n) time.
    """
    seen = {}  # number -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
    
    return []  # No solution found (shouldn't happen per constraints)
```

### Explanation

We iterate through the array once. For each number, we calculate its complement (target - num). If the complement has been seen before, we found our pair! Otherwise, we store the current number and its index for future lookups.

**Time Complexity**: O(n) - single pass through array
**Space Complexity**: O(n) - hash map stores up to n elements

### Why This Works

The key insight is that we don't need to check all pairs. We can:
1. Look at each number once
2. For each number, check if its "partner" (complement) exists
3. Use a hash map for O(1) lookup of the complement

### Common Mistakes

- ❌ Using nested loops (O(n²) - too slow)
- ❌ Sorting the array (changes indices)
- ❌ Not handling duplicates correctly (e.g., [3,3] target 6)

</details>

## Alternative Solutions

<details>
<summary>Alternative: Two Pointers (Only works if array is sorted)</summary>

```python
def two_sum_sorted(nums, target):
    """
    If array is sorted, use two pointers.
    Note: This changes the problem since we need original indices.
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []
```

**Trade-off**: O(n) time but requires sorted array. For this problem, hash map is better because we need original indices.

</details>

## Related Problems

- **Two Sum II** (LeetCode 167) - Input array is sorted
- **3Sum** (LeetCode 15) - Find three numbers that sum to target
- **4Sum** (LeetCode 18) - Find four numbers that sum to target
- **Two Sum IV - BST** (LeetCode 653) - Two Sum in a Binary Search Tree

## Reflection Questions

After solving, consider:
1. Why is hash map better than nested loops here?
2. Could you solve 3Sum using a similar approach?
3. What if the array had duplicates and we needed all pairs?
4. How would you explain this pattern to a beginner?

---

**Status**: [✓] Example Problem
**Pattern**: Hash Map for complement lookup
**Key Insight**: Store what you've seen to check complements in O(1) time


# Exercise 09 — Big-O Analysis
# ============================================================
# TASK: For each function below, write the TIME and SPACE
#       complexity in the comment block provided.
#
# FORMAT:
#   # Time:  O(?)
#   # Space: O(?)
#   # Reason: one sentence explaining why
#
# RULES:
#   - Do NOT run the code — analyze by reading only
#   - Ignore constants (3n → O(n), n/2 → O(n))
#   - Keep dominant term only (n² + n → O(n²))
#   - Space = extra memory used, NOT counting the input
#
# HINT: Ask yourself —
#   "How many times does the inner-most line execute?"
#   "What grows as n grows?"
# ============================================================


# ── Snippet 1 ────────────────────────────────────────────────
def snippet_1(nums: list[int]) -> int:
    return nums[0] + nums[-1]

# Time:  O(1)
# Space: O(1)
# Reason: since we are accessing these items via index


# ── Snippet 2 ────────────────────────────────────────────────
def snippet_2(nums: list[int]) -> list[int]:
    result = []
    for num in nums:
        if num % 2 == 0:
            result.append(num)
    return result

# Time:  O(n)
# Space: O(n)
# Reason: there is only one loop, so every item is getting looked at


# ── Snippet 3 ────────────────────────────────────────────────
def snippet_3(n: int) -> bool:
    i = 1
    while i < n:
        i *= 2
    return True

# Time:  O(log n)
# Space: O(1)
# Reason: since we are multiplying the i by 2 so the loop will go bellow n times


# ── Snippet 4 ────────────────────────────────────────────────
def snippet_4(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Time:  O(n)
# Space: O(n)
# Reason:for worst case scenario


# ── Snippet 5 ────────────────────────────────────────────────
def snippet_5(matrix: list[list[int]]) -> int:
    total = 0
    for row in matrix:
        for val in row:
            total += val
    return total

# Note: matrix is n×n (n rows, n columns)

# Time:  O(n^2)
# Space: O(1)
# Reason: n for rows and m for cols


# ── Snippet 6 ────────────────────────────────────────────────
def snippet_6(nums: list[int]) -> list[list[int]]:
    result = []
    n = len(nums)
    for i in range(n):
        for j in range(n):
            result.append([nums[i], nums[j]])
    return result

# Time:  O(n^2)
# Space: O(n^2)
# Reason: for both n for rows and n for cols

# Exercise 10 — Recursion
# ============================================================
# TASK: Implement each function using RECURSION only.
#
# RULES:
#   - No loops allowed (no for, no while)
#   - Every function must have a base case and recursive case
#   - Add Time and Space complexity at the bottom of each
#
# RECIPE for each problem:
#   1. What is the base case? (when do I stop?)
#   2. What does one call do? (one step of work)
#   3. Trust the recursion — assume smaller call works
# ============================================================


# ── Problem 1 — Factorial ────────────────────────────────────
# Return n! (n factorial)
# factorial(5) → 120  (5 * 4 * 3 * 2 * 1)
# factorial(0) → 1    (by definition)
# factorial(1) → 1
#
# Hint: n! = n * (n-1)!

def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n-1)

# Time:  O(n)
# Space: O(n) since in every frame there is a new n 


# ── Problem 2 — Digit Sum ────────────────────────────────────
# Return the sum of all digits in a non-negative integer.
# digit_sum(123)  → 6   (1 + 2 + 3)
# digit_sum(9)    → 9
# digit_sum(0)    → 0
#
# Hint: last digit = n % 10, remaining = n // 10

def digit_sum(n: int) -> int:
    if n == 0:
        return 0
    return (n % 10) + digit_sum(n//10)

# Time:  O(log n)
# Space: O(n)


# ── Problem 3 — Power ────────────────────────────────────────
# Return base raised to the power exp (base^exp).
# power(2, 10) → 1024
# power(3, 0)  → 1    (anything to the power 0 is 1)
# power(5, 1)  → 5
#
# Hint: base^exp = base * base^(exp-1)

def power(base: int, exp: int) -> int:
    if exp == 0:
        return 1
    return base * power(base=base,exp=exp-1)

# Time:  O(n)
# Space: O(n) since n will be created n times


# ── Problem 4 — Reverse String ───────────────────────────────
# Return the string reversed.
# reverse_string("hello") → "olleh"
# reverse_string("a")     → "a"
# reverse_string("")      → ""
#
# Hint: reverse("hello") = reverse("ello") + "h"
#       i.e. reverse the tail, then append the head

def reverse_string(s: str) -> str:
    if len(s)<=1:
        return s
    return reverse_string(s[1:]) +s[0]

# Time:  O(n)
# Space: O(n)

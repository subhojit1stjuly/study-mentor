# Exercise 05 — Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window + Hash Map (combined!)
#
# TASK:
#   Given a string, find the length of the longest substring
#   that contains NO repeating characters.
#
# RULES:
#   - A substring is a contiguous part of the string
#   - Aim for O(n) — no nested loops that re-scan characters
#
# EXAMPLES:
#   length_of_longest_substring("abcabcbb")  → 3   ("abc")
#   length_of_longest_substring("bbbbb")     → 1   ("b")
#   length_of_longest_substring("pwwkew")    → 3   ("wke")
#   length_of_longest_substring("")          → 0
#
# Time Complexity goal: O(n)
# Space Complexity goal: O(n)   ← you'll need extra storage this time
#
# THIS IS A COLD TEST — no pattern name given.
# Figure out what approach fits, then code it.
#
# THINK ABOUT THIS FIRST (before writing any code):
#   Imagine you have a window [left, right] sliding over the string.
#   As you expand right, what forces you to shrink from the left?
#   How do you know WHERE to move left to when a repeat is found?


def length_of_longest_substring(s: str) -> int:
   left,max_len = 0,0
   window = {}
   for right in range(len(s)):
      while s[right] in window:
         window.pop(s[left])
         left += 1
      window[s[right]] = 1
      max_len = max(max_len, right - left + 1) 
   return max_len

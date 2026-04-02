# Exercise 03 — Valid Palindrome
# Difficulty: Easy
# Topic: Two Pointers, Strings
#
# TASK:
#   A phrase is a palindrome if, after converting all uppercase letters
#   to lowercase and removing all non-alphanumeric characters, it reads
#   the same forward and backward.
#
#   Given a string, return True if it is a palindrome, False otherwise.
#
# RULES:
#   - Ignore spaces, punctuation, and capitalization
#   - Do NOT reverse the string with slicing [::-1] and compare —
#     use TWO POINTERS (one from the left, one from the right)
#   - Alphanumeric = letters (a-z, A-Z) and digits (0-9)
#
# EXAMPLES:
#   is_palindrome("A man, a plan, a canal: Panama")  → True
#   is_palindrome("race a car")                      → False
#   is_palindrome(" ")                               → True
#
# USEFUL PYTHON METHODS (you may use these):
#   "A".lower()         → "a"
#   "a".isalnum()       → True   (is alphanumeric?)
#   "!".isalnum()       → False
#
# Time Complexity goal: O(n)
# Space Complexity goal: O(1)
#
# HINT — The Two Pointer Idea:
#   Imagine two people walking toward each other from both ends of the string.
#   They skip non-letter/digit characters.
#   At each step they check: are the characters at my position the same?
#   If they ever disagree → not a palindrome.
#   If they meet in the middle without disagreeing → it IS a palindrome.


def is_palindrome(s: str) -> bool:
    right = len(s) - 1
    left = 0
    while left < right:
        while not s[left].isalnum():
            left += 1
        while not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True
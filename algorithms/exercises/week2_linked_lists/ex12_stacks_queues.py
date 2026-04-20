# Exercise 12 — Stacks & Queues
# ============================================================
# TASK: Implement each function below.
#
# ALLOWED IMPORTS:
#   from collections import deque   (for queue problems)
#
# RULES:
#   - Use list as a stack (append / pop)
#   - Use deque as a queue (append / popleft)
#   - No other data structures unless specified
#   - Add Time and Space complexity for each
# ============================================================

from collections import deque


# ── Problem 1 — Valid Parentheses ────────────────────────────
# Return True if every opening bracket has a matching closing
# bracket in the correct order.
#
# is_valid("()")      → True
# is_valid("()[]{}")  → True
# is_valid("([)]")    → False
# is_valid("{[]}")    → True
# is_valid("]")       → False
#
# Hint: use a stack. Push opening brackets, pop on closing.

def is_valid(s: str) -> bool:
    suported_parenthesis = {')':'(', ']':'[', '}':'{'}
    stack = []
    for ch in s:
        if ch in "({[":
            stack.append(ch)
        else:
            if not stack or stack[-1] != suported_parenthesis[ch]:
                return False
            stack.pop()
    return len(stack) == 0
# Time:  O(n)
# Space: O(1)


# ── Problem 2 — Reverse a String Using a Stack ───────────────
# Reverse a string using an explicit stack (not slicing!).
# reverse_string("hello") → "olleh"
# reverse_string("a")     → "a"
# reverse_string("")      → ""
#
# Hint: push all chars onto stack, then pop them all off

def reverse_string(s: str) -> str:
    ans = ""
    stack = []
    for ch in s:
        stack.append(ch)
    while stack:
        ans += stack.pop()
    return ans


# Time:  O(n) = O(n+n)
# Space: O(1) = Constant


# ── Problem 3 — Implement a Queue Using Two Stacks ───────────
# Implement a Queue with enqueue and dequeue operations
# using only two Python lists (stacks). No deque allowed here.
#
# q = MyQueue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.dequeue() → 1   (FIFO — first in, first out)
# q.dequeue() → 2
#
# Hint: stack1 receives new items (enqueue)
#       To dequeue, pour stack1 into stack2 (reverses order)
#       Then pop from stack2

class MyQueue:
    def __init__(self):
        self.stack1: list[int] = []   # for enqueue
        self.stack2: list[int] = []   # for dequeue

    def enqueue(self, val: int) -> None:
        self.stack1.append(val)

    def dequeue(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

# enqueue Time:  O(1)
# dequeue Time:  O(n) amortized
# Space:         O(1)


# ── Problem 4 — Daily Temperatures ──────────────────────────
# Given a list of daily temperatures, return a list where
# each element is the number of days until a warmer temperature.
# If no warmer day exists, put 0.
#
# daily_temperatures([73,74,75,71,69,72,76,73]) → [1,1,4,2,1,1,0,0]
# daily_temperatures([30,40,50,60])             → [1,1,1,0]
# daily_temperatures([30,60,90])                → [1,1,0]
#
# Hint: monotonic stack — store indices, not values
#       When you find a warmer day, pop and record the gap

# --- Initial --- ans = [0,0,0,0,0,0,0,0], stack = [] 
# --- i = 0 ----- ans = [0,0,0,0,0,0,0,0], stack = [0] temparature = 73
# --- i = 1 ----- ans = [1,0,0,0,0,0,0,0], stack = [1] temparature = 74
# --- i = 2 ----- ans = [1,1,0,0,0,0,0,0], stack = [2] temparature = 75
# --- i = 3 ----- ans = [1,1,0,0,0,0,0,0], stack = [0] temparature = 71
# --- i = 4 ----- ans = [1,1,0,0,0,0,0,0], stack = [0] 
# --- i = 5 ----- ans = [1,1,0,0,0,0,0,0], stack = [0] 
# --- i = 6 ----- ans = [1,1,0,0,0,0,0,0], stack = [0] 
# --- i = 7 ----- ans = [1,1,0,0,0,0,0,0], stack = [0] 

def daily_temperatures(temperatures: list[int]) -> list[int]:
    ans = [0] * len(temperatures)
    stack = []
    for i in range(len(temperatures)):
        if not stack:
            stack.append(i)
        else:
            while stack:
                peek = stack[len(stack) - 1]
                if temperatures[i] > temperatures[peek]:
                    ans[peek] =  i - peek
                    stack.pop()
                else:
                    break
            stack.append(i)
    return ans

# Time:  O(?)
# Space: O(?)

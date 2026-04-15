# Exercise 11 — Linked Lists
# ============================================================
# TASK: Implement each function below.
#
# The Node class is provided — do NOT modify it.
# You may use helper functions if needed.
#
# RULES:
#   - No converting to array/list and back
#   - Solve in-place where possible
#   - Add Time and Space complexity for each
# ============================================================


class Node:
    def __init__(self, val: int = 0, next: "Node | None" = None):
        self.val = val
        self.next = next


# ── Problem 1 — Print List ───────────────────────────────────
# Traverse the list and return all values as a Python list.
# print_list(1→2→3→4→5) → [1, 2, 3, 4, 5]
# print_list(None)       → []
#
# Hint: start at head, follow .next until None

def to_list(head: Node | None) -> list[int]:
    ans = []
    while head != None:
        ans.append(head.val)
        head = head.next
    return ans

# Time:  O(n)
# Space: O(1)


# ── Problem 2 — Reverse List ─────────────────────────────────
# Reverse a singly linked list in-place. Return the new head.
# 1→2→3→4→5 → 5→4→3→2→1
# None       → None
# 1          → 1
#
# Hint: three pointers — prev, curr, next_node

def reverse_list(head: Node | None) -> Node | None:
    prev = None
    curr = head
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev
# Time:  O(?)
# Space: O(?)


# ── Problem 3 — Find Middle ──────────────────────────────────
# Return the MIDDLE node of the linked list.
# If even length, return the SECOND middle node.
# 1→2→3→4→5  → node with val 3
# 1→2→3→4    → node with val 3  (second middle)
# 1           → node with val 1
#
# Hint: slow + fast pointer (Floyd's)
#       When fast reaches end, slow is at middle

def find_middle(head: Node | None) -> Node | None:
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow
# Time:  O(n)
# Space: O(2)


# ── Problem 4 — Has Cycle ────────────────────────────────────
# Return True if the linked list has a cycle, False otherwise.
# A cycle means some node's .next points back to a previous node.
#
# Hint: slow + fast pointer
#       If they ever meet → cycle exists
#       If fast reaches None → no cycle

def has_cycle(head: Node | None) -> bool:
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False

# Time:  O(n)
# Space: O(2)

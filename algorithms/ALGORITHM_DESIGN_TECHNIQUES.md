# Algorithm Design Techniques

This document outlines the high-level paradigms for designing algorithms. Use this to decide on the overall "architecture" of your solution before picking a specific coding pattern.

---

## 1. Brute Force

The most straightforward, "obvious" solution that exhaustively checks every possibility.

-   **Strategy:** Generate every possible solution and check if it satisfies the problem's constraints.
-   **When to use:**
    -   As a starting point to understand the problem.
    -   When the input size is very small and a simple solution is sufficient.
    -   To verify the correctness of an optimized solution on small test cases.
-   **Example:** To find a pair that sums to a target in an array, check every possible pair of numbers.
-   **Complexity:** Often high (e.g., $O(n^2)$, $O(n!)$, $O(2^n)$).

---

## 2. Greedy Algorithms

Make the locally optimal choice at each step with the hope of finding a global optimum.

-   **Strategy:** At each stage, make the choice that looks best *at that moment*. You never reconsider previous choices.
-   **When to use:**
    -   When a problem has the **Greedy Choice Property**: a global optimum can be arrived at by selecting a local optimum.
    -   When a problem has the **Optimal Substructure Property**: an optimal solution to the problem contains optimal solutions to subproblems.
-   **Key Indicators:** "Maximize/minimize...", "find the largest/smallest...", "select activities...".
-   **Example:** Finding the minimum number of coins to make change. At each step, take the largest coin smaller than the remaining amount.
-   **Complexity:** Often very fast (e.g., $O(n)$ or $O(n \log n)$ if sorting is needed).

---

## 3. Divide and Conquer

Break the problem down into smaller, independent subproblems of the same type, solve them recursively, and then combine their solutions.

-   **Strategy:**
    1.  **Divide:** Break the problem into smaller subproblems.
    2.  **Conquer:** Solve the subproblems recursively. If they are small enough, solve them directly.
    3.  **Combine:** Merge the solutions of the subproblems to get the solution for the original problem.
-   **When to use:**
    -   When the problem can be naturally split into non-overlapping subproblems.
-   **Key Indicators:** The problem structure lends itself to recursion. Often seen with sorted data.
-   **Example:** Merge Sort, Quick Sort, Binary Search.
-   **Complexity:** Typically follows the form $T(n) = aT(n/b) + f(n)$, often resulting in $O(n \log n)$.

---

## 4. Dynamic Programming (DP)

Break the problem down into smaller, **overlapping** subproblems, solve each subproblem just once, and store their solutions to avoid re-computation.

-   **Strategy:**
    -   **Top-Down (Memoization):** Solve recursively, but store results in a cache (e.g., a hash map or array) to avoid re-solving the same subproblem.
    -   **Bottom-Up (Tabulation):** Solve the smallest subproblems first and use their results to build up solutions to larger ones, typically using an array or matrix.
-   **When to use:**
    -   When a problem has **Optimal Substructure** (like Greedy).
    -   When a problem has **Overlapping Subproblems** (unlike Divide and Conquer).
-   **Key Indicators:** "Find the number of ways...", "find the minimum/maximum cost...", "find the longest/shortest path...". Often involves sequences, grids, or states.
-   **Example:** Fibonacci sequence, Longest Common Subsequence, Knapsack problem.
-   **Complexity:** Depends on the number of states and transitions, e.g., $O(n^2)$ for Longest Common Subsequence.

---

## 5. Backtracking

Explore all potential solutions incrementally and abandon a path ("backtrack") as soon as it is determined that it cannot lead to a valid solution.

-   **Strategy:** Build a solution step-by-step using recursion. If a step leads to a dead end, undo it and try the next alternative. It's a refined brute force that prunes the search space.
-   **When to use:**
    -   For problems that require finding all possible solutions (e.g., permutations, combinations).
    -   For constraint satisfaction problems (e.g., Sudoku, N-Queens).
-   **Key Indicators:** "Find all possible...", "generate all permutations/combinations...", "solve this puzzle...".
-   **Example:** Generating all permutations of a set, solving a Sudoku puzzle.
-   **Complexity:** Can be high (e.g., $O(n!)$), but often better than pure brute force due to pruning.

---

## 6. Two Pointers / Sliding Window

A specialized and efficient technique for array and string problems.

-   **Strategy:** Use two pointers to define a "window" or range within the data. Move the pointers based on certain conditions to explore subarrays/substrings in linear time.
-   **When to use:**
    -   **Two Pointers:** On sorted arrays to find pairs, or for in-place modifications from both ends.
    -   **Sliding Window:** To find the longest/shortest subarray/substring that satisfies a condition.
-   **Example:** Valid Palindrome (Two Pointers), Longest Substring Without Repeating Characters (Sliding Window).
-   **Complexity:** $O(n)$.

---

## 7. Data Structure-Driven Design

The choice of a specific data structure is the core of the algorithm's design.

-   **Strategy:** Identify a property of the problem that maps perfectly to a data structure's strengths. The algorithm then becomes a series of operations on that data structure.
-   **When to use:**
    -   When you need efficient retrieval of min/max elements (**Heap / Priority Queue**).
    -   When you need to store and search for strings by prefix (**Trie**).
    -   When you need to manage disjoint sets (**Union-Find**).
    -   When you need to maintain order and allow efficient lookups (**Balanced Binary Search Tree / TreeMap**).
-   **Example:** Finding the median of a data stream (using two heaps), implementing an autocomplete system (using a Trie).
-   **Complexity:** Depends entirely on the chosen data structure's operation complexities.

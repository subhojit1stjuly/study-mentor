---
name: dsa-mastery
description: "Use when: studying data structures and algorithms, learning DSA roadmap, practicing coding problems, mastering sorting algorithms, learning graph algorithms, studying dynamic programming, understanding trees and heaps, preparing for coding interviews, competitive programming, studying time and space complexity, Big-O analysis."
argument-hint: "Topic or phase to study (e.g., 'binary search', 'Phase 3 graphs', 'DP patterns')"
---

# DSA Mastery Roadmap

A structured, phase-based roadmap for mastering Data Structures and Algorithms — from fundamentals through advanced competitive programming topics.

## When to Use

- Starting or resuming a DSA study journey
- Requesting a structured study plan for algorithms
- Diving deep into a specific data structure or algorithm
- Preparing for coding interviews (FAANG/MAANG)
- Practicing competitive programming
- Reviewing and self-assessing DSA knowledge

## How This Skill Works

1. **Assess** the user's current DSA level (beginner / intermediate / advanced)
2. **Place** them in the appropriate phase
3. **Teach** with theory → code → trace → practice
4. **Assign** LeetCode/HackerRank problems after each module
5. **Assess** understanding with checkpoint questions before advancing
6. **Track** progress using the todo list and workspace files

---

## Phase 0: Foundations

> **Goal**: Build the mathematical and analytical foundation for algorithm analysis.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 0.1 | Complexity Analysis | Big-O, Big-Theta, Big-Omega, amortized analysis, best/average/worst case, common complexities ($O(1)$ → $O(n!)$), comparing growth rates |
| 0.2 | Recursion | Base cases, recursive calls, call stack visualization, tail recursion, recursion tree method, converting recursion ↔ iteration |
| 0.3 | Math for DSA | Logarithms, summation formulas, geometric/arithmetic series, modular arithmetic, GCD/LCM, combinatorics basics, master theorem |

### Checkpoint
- Analyze the time complexity of 5 different code snippets
- Convert a recursive function to iterative and vice versa
- Apply the master theorem to 3 recurrence relations

---

## Phase 1: Linear Data Structures

> **Goal**: Master arrays, linked lists, stacks, queues, and their applications.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 1.1 | Arrays & Strings | Static vs dynamic arrays, 2D arrays, string manipulation, in-place operations, sliding window, two pointers, prefix sums |
| 1.2 | Linked Lists | Singly, doubly, circular, sentinel nodes, fast/slow pointers, cycle detection (Floyd's), merge two lists, reverse in-place, LRU cache |
| 1.3 | Stacks | LIFO, implementation (array/linked list), monotonic stack, next greater element, valid parentheses, min stack, expression evaluation (infix, postfix) |
| 1.4 | Queues & Deques | FIFO, circular queue, deque, monotonic deque, sliding window maximum, BFS foundation, priority queue intro |

### Practice Problems (per module)
- **Easy** (3): Build familiarity with the data structure
- **Medium** (5): Apply patterns (two pointers, sliding window, stack tricks)
- **Hard** (2): Combine multiple concepts

### Checkpoint
- Implement a dynamic array from scratch with amortized $O(1)$ append
- Solve "LRU Cache" (LeetCode 146) from scratch
- Explain when to use a stack vs queue vs deque with real examples

---

## Phase 2: Hashing & Sorting

> **Goal**: Master hash-based structures and all major sorting algorithms.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 2.1 | Hash Tables | Hash functions, collision resolution (chaining, open addressing, Robin Hood), load factor, resizing, hash map implementation from scratch |
| 2.2 | Hash Applications | Two sum patterns, frequency counting, anagram grouping, subarray sum equals K, consistent hashing, Bloom filters |
| 2.3 | Comparison Sorts | Bubble, selection, insertion (and their uses), merge sort (divide & conquer), quick sort (partitioning schemes: Lomuto, Hoare), heap sort |
| 2.4 | Non-Comparison Sorts | Counting sort, radix sort, bucket sort — when they beat $O(n \log n)$ |
| 2.5 | Sorting Applications | Stability, in-place vs out-of-place, custom comparators, merge intervals, meeting rooms, Dutch national flag |

### Checkpoint
- Implement a hash map from scratch with chaining
- Implement merge sort and quick sort from scratch, explain the trade-offs
- Solve 3 problems where sorting is the key insight

---

## Phase 3: Trees & Heaps

> **Goal**: Master tree-based data structures and heap/priority queue patterns.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 3.1 | Binary Trees | Traversals (inorder, preorder, postorder, level-order), recursive vs iterative, tree construction from traversals, diameter, height, LCA |
| 3.2 | Binary Search Trees | BST property, insert/delete/search, validation, inorder successor, balanced vs unbalanced, BST to sorted array |
| 3.3 | Balanced BSTs | AVL trees (rotations), Red-Black trees (properties), when each is used in practice (e.g., Java TreeMap, C++ map) |
| 3.4 | Heaps & Priority Queues | Binary heap (min/max), heapify ($O(n)$ vs $O(n \log n)$), heap sort, top-K problems, merge K sorted lists, median finder (two heaps) |
| 3.5 | Tries | Prefix tree implementation, insert/search/startsWith, auto-complete, word search, XOR trie for maximum XOR |
| 3.6 | Advanced Trees | Segment trees (range queries, point updates, lazy propagation), Fenwick trees (BIT), interval trees |

### Checkpoint
- Implement a BST with insert, delete, search, and inorder traversal
- Implement a min-heap from scratch
- Solve "Word Search II" (LeetCode 212) using tries
- Implement a segment tree with range sum query

---

## Phase 4: Graphs

> **Goal**: Master graph representations, traversals, and classic graph algorithms.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 4.1 | Graph Basics | Representations (adjacency list, matrix, edge list), directed/undirected, weighted/unweighted, connected components, degree |
| 4.2 | BFS & DFS | Traversal implementation, shortest path in unweighted graph, cycle detection (directed & undirected), connected components, bipartite check |
| 4.3 | Topological Sort | Kahn's algorithm (BFS), DFS-based, course schedule problems, build order, detecting cycles in DAGs |
| 4.4 | Shortest Paths | Dijkstra's (priority queue), Bellman-Ford (negative weights), Floyd-Warshall (all pairs), 0-1 BFS, A* search |
| 4.5 | Minimum Spanning Trees | Prim's algorithm, Kruskal's algorithm (with Union-Find), cut property, applications |
| 4.6 | Union-Find | Disjoint set implementation, path compression, union by rank, applications (connected components, Kruskal's, cycle detection) |
| 4.7 | Advanced Graphs | Strongly connected components (Tarjan's, Kosaraju's), articulation points & bridges, Euler paths, max flow (Ford-Fulkerson), bipartite matching |

### Checkpoint
- Implement BFS and DFS for both adjacency list and matrix
- Implement Dijkstra's from scratch with a priority queue
- Solve "Number of Islands" (BFS/DFS), "Course Schedule" (topological sort), "Network Delay Time" (Dijkstra's)
- Implement Union-Find with path compression and union by rank

---

## Phase 5: Dynamic Programming

> **Goal**: Master DP thinking — identify subproblems, write recurrences, optimize.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 5.1 | DP Fundamentals | Overlapping subproblems, optimal substructure, memoization (top-down) vs tabulation (bottom-up), state definition, base cases |
| 5.2 | 1D DP | Fibonacci, climbing stairs, house robber, coin change, longest increasing subsequence, word break |
| 5.3 | 2D DP | Grid paths, edit distance, longest common subsequence, longest common substring, matrix chain multiplication, palindrome partitioning |
| 5.4 | Knapsack Patterns | 0/1 knapsack, unbounded knapsack, subset sum, partition equal subset sum, target sum, coin change variations |
| 5.5 | Interval DP & Trees | Burst balloons, matrix chain multiplication, DP on trees (tree diameter, house robber III), rerooting technique |
| 5.6 | State Optimization | Space optimization (rolling array), bitmask DP (traveling salesman), digit DP, profile DP |

### DP Problem-Solving Framework
```
1. DEFINE STATE  → What does dp[i] (or dp[i][j]) represent?
2. RECURRENCE    → How does dp[i] relate to smaller subproblems?
3. BASE CASES    → What are the trivial cases?
4. ORDER         → What order to fill the table? (or use memoization)
5. ANSWER        → Which cell contains the final answer?
6. OPTIMIZE      → Can we reduce space? Time?
```

### Checkpoint
- Solve 5 classic DP problems explaining the state definition and recurrence
- Convert a top-down solution to bottom-up and vice versa
- Optimize a 2D DP solution to use $O(n)$ space

---

## Phase 6: Advanced Techniques

> **Goal**: Master patterns and techniques that appear in hard interview problems and competitive programming.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 6.1 | Greedy Algorithms | Activity selection, fractional knapsack, Huffman coding, interval scheduling, jump game, task scheduler — proving greedy works (exchange argument) |
| 6.2 | Backtracking | N-Queens, Sudoku solver, permutations, combinations, subsets, word search, constraint satisfaction |
| 6.3 | Binary Search on Answer | Koko eating bananas, split array largest sum, capacity to ship packages, aggressive cows — identifying "monotonic predicate" pattern |
| 6.4 | Bit Manipulation | AND/OR/XOR properties, counting bits, single number problems, power of two, bitmask subsets, XOR tricks |
| 6.5 | String Algorithms | KMP (failure function), Rabin-Karp (rolling hash), Z-algorithm, longest palindromic substring (Manacher's), edit distance |
| 6.6 | Divide & Conquer | Merge sort applications (count inversions, closest pair), quick select (Kth largest), matrix exponentiation, meet in the middle |

### Checkpoint
- Solve a "binary search on answer" problem and explain the monotonic predicate
- Implement KMP string matching from scratch
- Solve a backtracking problem with pruning optimization

---

## Phase 7: Interview Problem Patterns

> **Goal**: Recognize and apply the 15 most common coding interview patterns.

| Pattern | Core Idea | Classic Problems |
|---------|-----------|-----------------|
| Sliding Window | Fixed/variable window over array | Max subarray sum, longest substring without repeating chars |
| Two Pointers | Converging or parallel pointers | Container with most water, 3Sum, remove duplicates |
| Fast & Slow Pointers | Cycle detection, middle finding | Linked list cycle, happy number, find duplicate |
| Merge Intervals | Sort + merge overlapping | Meeting rooms, insert interval, employee free time |
| Cyclic Sort | Place elements at correct index | Find missing/duplicate number, first missing positive |
| In-place Reversal | Reverse linked list segments | Reverse nodes in k-group, palindrome linked list |
| BFS/DFS | Tree/graph traversal | Level order, number of islands, word ladder |
| Two Heaps | Median tracking, scheduling | Find median from data stream, IPO |
| Subsets/Permutations | Backtracking enumeration | Power set, letter combinations, palindrome partitioning |
| Modified Binary Search | Search in sorted/rotated arrays | Search rotated array, peak element, first bad version |
| Top K Elements | Heap or quick select | Kth largest, top K frequent, K closest points |
| K-way Merge | Merge sorted structures | Merge K sorted lists, smallest range covering K lists |
| Topological Sort | Dependency ordering | Course schedule, alien dictionary |
| Dynamic Programming | Optimal substructure + overlapping | See Phase 5 |
| Monotonic Stack/Queue | Next greater/smaller element | Daily temperatures, largest rectangle in histogram |

---

## Study Method for Every Topic

```
1. THEORY    → Understand the concept, draw diagrams
2. IMPLEMENT → Code the data structure/algorithm from scratch
3. TRACE     → Walk through with a concrete example step by step
4. PRACTICE  → Solve 5-10 problems (Easy → Medium → Hard)
5. PATTERNS  → Identify which pattern this problem uses
6. REVIEW    → Revisit after 3 days, then 7 days (spaced repetition)
```

## Progress Tracking

- Save notes under `algorithms/` folder in the workspace
- Create `algorithms/progress.md` to track completed modules
- Use the todo list for current study sessions
- Log solved problems with difficulty, pattern, and time taken

## Recommended Resources

| Resource | Type | Best For |
|----------|------|----------|
| NeetCode 150 | Problem list | Interview patterns (curated) |
| Blind 75 | Problem list | Core interview problems |
| LeetCode | Platform | Practice (Easy → Hard) |
| Codeforces | Platform | Competitive programming |
| CLRS (Cormen) | Book | Deep algorithmic theory |
| Algorithm Design Manual (Skiena) | Book | Practical algorithm selection |
| Abdul Bari (YouTube) | Video | Visual algorithm explanations |
| William Fiset (YouTube) | Video | Graph algorithms deep dives |

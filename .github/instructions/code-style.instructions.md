---
applyTo: "**/*.py"
description: "Python code style conventions for study implementations and algorithm practice."
---

## Python Code Conventions

- Use **type hints** for all function signatures
- Use **meaningful variable names** (no single letters except loop counters `i`, `j`, `k` and math conventions `n`, `m`)
- Include a **docstring** for functions that implement algorithms or data structures
- Include **Big-O complexity** as a comment at the top of algorithm implementations:
  ```python
  # Time: O(n log n), Space: O(n)
  ```
- Use **snake_case** for functions and variables, **PascalCase** for classes
- Prefer **list comprehensions** over map/filter when readable
- Use `from __future__ import annotations` for forward references when needed
- Keep implementations clean and educational — prioritize readability over cleverness

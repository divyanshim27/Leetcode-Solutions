# 🚀 Daily DSA Learnings & Key Takeaways

A centralized dump for key algorithmic patterns, Python shortcuts, edge cases, and time complexity notes.

---

## 🧠 Core Patterns & Python Cheat Sheet

### 1. Hash Maps / Dictionaries
* **Two Sum Pattern ($O(N)$ Time, $O(N)$ Space):** Instead of nested loops ($O(N^2)$), compute `complement = target - current` and check if `complement` exists in a hash map.
* **Frequency Counting:** Use `collections.Counter(arr)` or `collections.defaultdict(int)` to avoid key errors.

### 2. Sets for Uniqueness
* **Contains Duplicate Pattern ($O(N)$ Time, $O(N)$ Space):** Sets provide $O(1)$ lookup time. Comparing `len(nums) != len(set(nums))` instantly identifies duplicates.

---

## 📝 Daily Log

### 📅 Day 1 — Hash Maps & Sets
* **Problems Solved:** LC 1 (Two Sum), LC 217 (Contains Duplicate)
* **Key Learnings:**
  * Trade space complexity ($O(N)$ hash set/dict) to achieve linear time complexity ($O(N)$) over brute force $O(N^2)$.
  * Python's `enumerate(nums)` yields both index and value cleanly.

---

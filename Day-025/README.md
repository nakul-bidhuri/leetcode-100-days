# 📅 Day 025

## Problems Solved

### 1. Valid Triangle Number (LeetCode #611)

### Problem Statement

Given an integer array, count the number of triplets that can form a valid triangle.

A triangle is valid if:

a + b > c

### Approach

- Sort the array.
- Fix the largest side.
- Use two pointers to find valid pairs.
- Count all valid triplets.

### Complexity

- Time Complexity: O(n²)
- Space Complexity: O(1)

---

### 2. Pair with Target Sum

### Problem Statement

Given a sorted array and a target value, determine whether there exists a pair whose sum equals the target.

### Approach

- Use two pointers.
- Compare the sum.
- Move the left or right pointer depending on the result.
- Stop when the target is found.

### Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

---

# 🧠 Concepts Learned

- Sorting
- Two Pointers
- Triplet Counting
- Binary Search Thinking
- Efficient Searching

---

# 📚 Interview Questions

### Valid Triangle Number

- Why sort the array?
- Why add `(right - left)` instead of `1`?
- Why fix the largest side first?

### Pair with Target Sum

- Why use two pointers?
- Why does this work only for sorted arrays?
- What if the array is unsorted?

---

## ✅ Status

✔ Problem 1 Completed

✔ Problem 2 Completed

**Language Used:** Python 🐍
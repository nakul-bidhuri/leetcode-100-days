# 📅 Day 026

## Problems Solved

### 1. Sort Colors (LeetCode #75)

### Problem Statement

Given an array containing only 0s, 1s, and 2s, sort the array in-place without using any built-in sorting function.

### Approach

- Use three pointers:
  - low
  - mid
  - high
- Place 0s at the beginning.
- Leave 1s in the middle.
- Move 2s to the end.

### Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

---

### 2. Triplet Sum Check

### Problem Statement

Determine whether there exist three elements such that the sum of two elements equals the third element.

### Approach

- Sort the array.
- Fix one element as the target.
- Use two pointers to find whether two numbers sum to the target.

### Complexity

- Time Complexity: O(n²)
- Space Complexity: O(1)

---

# 🧠 Concepts Learned

- Dutch National Flag Algorithm
- Three Pointer Technique
- Two Pointers
- Sorting
- Triplet Search

---

# 📚 Interview Questions

### Sort Colors

- Why use three pointers?
- Why don't we increase `mid` after swapping with `high`?
- Why is this called the Dutch National Flag Algorithm?

### Triplet Sum Check

- Why sort the array first?
- Why use two pointers instead of three loops?
- Can duplicate values affect the answer?

---

## ✅ Status

✔ Problem 1 Completed

✔ Problem 2 Completed

**Language Used:** Python 🐍
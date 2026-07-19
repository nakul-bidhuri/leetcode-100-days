# 📅 Day 024

## Problems Solved

### 1. Happy Number (LeetCode #202)

### Problem Statement

Given a positive integer, repeatedly replace the number with the sum of the squares of its digits.

If the process reaches 1, the number is happy.
Otherwise, it enters a cycle and is not happy.

### Approach

- Extract every digit.
- Find the square of each digit.
- Repeat the process.
- Use a set to detect cycles.

### Complexity

- Time Complexity: O(log n)
- Space Complexity: O(log n)

---

### 2. Squares of a Sorted Array (LeetCode #977)

### Problem Statement

Given a sorted array, return another sorted array containing the square of every number.

### Approach

- Use two pointers.
- Compare absolute values at both ends.
- Place the larger square at the end.
- Continue until all elements are processed.

### Complexity

- Time Complexity: O(n)
- Space Complexity: O(n)

---

# 🧠 Concepts Learned

- Cycle Detection
- Mathematical Simulation
- Digit Extraction
- Two Pointers
- Array Traversal

---

# 📚 Interview Questions

### Happy Number

- Why use a set?
- Why does the process eventually repeat?
- Can Floyd's Cycle Detection be used?

### Squares of Sorted Array

- Why compare absolute values?
- Why fill the result array from the end?
- Why not simply square every element?

---

## ✅ Status

✔ Problem 1 Completed

✔ Problem 2 Completed

**Language Used:** Python 🐍
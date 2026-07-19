# 📅 Day 023

## Problems Solved

### 1. Assign Cookies (LeetCode #455)

### Problem Statement

Given two arrays:

- g[] → greed factor of children
- s[] → cookie sizes

Assign cookies so that the maximum number of children are satisfied.

### Approach

- Sort both arrays.
- Use two pointers.
- Try giving the smallest possible cookie that satisfies each child.
- Count satisfied children.

### Complexity

- Time Complexity: O(n log n + m log m)
- Space Complexity: O(1)

---

### 2. Backspace Equality

### Problem Statement

Given two strings containing '#' characters, where '#' represents a backspace, determine whether both processed strings become equal.

### Approach

- Traverse each string.
- Use a stack.
- Remove the last character whenever '#' is found.
- Compare the final processed strings.

### Complexity

- Time Complexity: O(n + m)
- Space Complexity: O(n + m)

---

# 🧠 Concepts Learned

- Greedy Algorithm
- Sorting
- Two Pointers
- Stack
- String Processing

---

# 📚 Interview Questions

### Assign Cookies

- Why sort both arrays?
- Why give the smallest suitable cookie?
- Why is this a greedy algorithm?

### Backspace Equality

- Why use a stack?
- What happens if '#' appears first?
- Can this be solved using O(1) extra space?

---

## ✅ Status

✔ Problem 1 Completed

✔ Problem 2 Completed

**Language Used:** Python 🐍
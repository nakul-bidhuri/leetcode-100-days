# 📅 Day 003

## Problems Solved

### 1. Plus One (LeetCode #66)

**Problem Statement**

Given an integer array `digits`, where each element represents a digit of a large integer, increment the integer by one and return the resulting array.

### Approach

- Start traversing from the last digit.
- If the current digit is less than 9, increment it by one and return the array.
- If the current digit is 9, change it to 0 and carry 1 to the previous digit.
- If every digit is 9, return a new array with a leading 1.

### Algorithm

1. Traverse the array from right to left.
2. If `digits[i] < 9`
   - Increment it by 1.
   - Return the array.
3. Otherwise set it to `0`.
4. If the loop finishes, return `[1] + digits`.

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

### 2. Number of Occurrences

**Problem Statement**

Given a sorted array and a target value, count how many times the target appears in the array.

### Approach

- Traverse the array once.
- Compare every element with the target.
- Increase the counter whenever the target is found.
- Return the final count.

> **Note:** Since the array is sorted, this problem can also be solved using Binary Search in **O(log n)** time. The current solution is the beginner-friendly approach.

### Algorithm

1. Initialize `count = 0`.
2. Traverse the array.
3. If the current element equals the target, increment `count`.
4. Return `count`.

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

# 🧠 Concepts Learned

- Arrays
- Reverse Array Traversal
- Carry Propagation
- Number Simulation
- Array Traversal
- Counting Occurrences
- Time Complexity
- Space Complexity
- Introduction to Binary Search

---

# 📚 Interview Takeaways

### Plus One

- Why do we start from the last digit?
- How is carry handled?
- What happens when every digit is 9?

### Number of Occurrences

- Can you solve this in O(log n)?
- Why is Binary Search possible only because the array is sorted?
- Difference between Linear Search and Binary Search.

---

## ✅ Status

- ✔ Problem 1 Completed
- ✔ Problem 2 Completed

**Language Used:** Python 🐍
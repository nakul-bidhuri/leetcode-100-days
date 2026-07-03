# 📅 Day 006

## Problems Solved

### 1. House Robber II (LeetCode #213)

### Problem Statement

Given houses arranged in a circle, find the maximum money that can be robbed without robbing two adjacent houses.

### Approach

- Since the first and last houses are adjacent, we cannot rob both.
- Solve two separate cases:
  1. Rob houses from first to second-last.
  2. Rob houses from second to last.
- Return the maximum of the two results.

### Algorithm

1. Handle the single-house case.
2. Solve two linear House Robber problems.
3. Return the larger result.

### Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

---

### 2. Union of Two Sorted Arrays

### Problem Statement

Return the union of two sorted arrays with only distinct elements.

### Approach

- Use two pointers.
- Compare elements from both arrays.
- Add only unique elements to the result.
- Continue until both arrays are fully traversed.

### Complexity

- Time Complexity: O(n + m)
- Space Complexity: O(n + m)

---

# 🧠 Concepts Learned

- Dynamic Programming
- Circular Arrays
- State Optimization
- Two Pointer Technique
- Array Merging
- Duplicate Handling

---

# 📚 Interview Questions

### House Robber II

- Why do we split the problem into two cases?
- Why can't we rob both the first and last houses?
- Why is Dynamic Programming used?

### Union of Two Sorted Arrays

- Why use two pointers?
- How are duplicates removed?
- Why is sorting not required?

---

## ✅ Status

✔ Problem 1 Completed

✔ Problem 2 Completed

**Language Used:** Python 🐍
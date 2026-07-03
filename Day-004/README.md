# 📅 Day 004

## Problems Solved

### 1. Transpose Matrix (LeetCode #867)

### Problem Statement

Given a 2D integer matrix, return its transpose.

### Approach

- Traverse every column.
- For each column, traverse every row.
- Store the values in a new matrix.

### Algorithm

1. Count rows and columns.
2. Create an empty transpose matrix.
3. Traverse columns.
4. Traverse rows.
5. Store matrix[row][col] in the new matrix.
6. Return the transpose matrix.

### Complexity

- Time Complexity : O(rows × columns)
- Space Complexity : O(rows × columns)

---

### 2. Rotate Array by K Steps

### Problem Statement

Rotate the array to the right by **k** steps.

### Approach

- Calculate the effective rotation using modulus.
- Take the last k elements.
- Append the remaining elements.

### Algorithm

1. Find array length.
2. Compute `k = k % n`.
3. Take last k elements.
4. Append remaining elements.
5. Return rotated array.

### Complexity

- Time Complexity : O(n)
- Space Complexity : O(n)

---

# 🧠 Concepts Learned

- 2D Arrays
- Matrix Traversal
- Nested Loops
- Matrix Transformation
- Array Rotation
- List Slicing
- Modular Arithmetic

---

# 📚 Interview Questions

### Transpose Matrix

- What is a transpose?
- Why are nested loops required?
- Can we transpose a non-square matrix?

### Rotate Array

- Why do we use `k % n`?
- What happens if k is greater than the array size?
- Can you solve this in O(1) extra space?

---

## ✅ Status

✔ Problem 1 Completed

✔ Problem 2 Completed

**Language Used:** Python 🐍
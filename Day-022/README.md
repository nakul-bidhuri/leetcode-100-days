# 📅 Day 022

## Problems Solved

### 1. Move Zeroes (LeetCode #283)

### Problem Statement

Move all zeroes to the end of the array while maintaining the relative order of non-zero elements.

### Approach

- Use two pointers.
- One pointer keeps track of where the next non-zero element should go.
- Traverse the array once.
- Swap non-zero elements into their correct positions.

### Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

---

### 2. Card Game Strategy

### Problem Statement

Two players take turns choosing either the leftmost or rightmost card.

Each player always chooses the larger card available at either end.

Return the final scores of both players.

### Approach

- Use two pointers.
- Compare both ends.
- Pick the larger value.
- Alternate turns until no cards remain.

### Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

---

# 🧠 Concepts Learned

- Two Pointer Technique
- Array Manipulation
- Greedy Algorithm
- Simulation
- In-place Swapping

---

# 📚 Interview Questions

### Move Zeroes

- Why use two pointers?
- Why swap instead of creating a new array?
- Can this be solved in one pass?

### Card Game Strategy

- Why compare only the two ends?
- Is choosing the larger end always the best strategy?
- What if both players played optimally instead of greedily?

---

## ✅ Status

✔ Problem 1 Completed

✔ Problem 2 Completed

**Language Used:** Python 🐍
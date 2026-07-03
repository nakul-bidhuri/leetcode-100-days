# 📅 Day 005

## Problems Solved

### 1. Jump Game (LeetCode #55)

### Problem Statement

Given an array where each element represents the maximum jump length, determine whether you can reach the last index.

### Approach

- Keep track of the farthest index that can be reached.
- Traverse the array once.
- If the current index is greater than the farthest reachable index, return False.
- Otherwise, update the farthest reachable index.

### Algorithm

1. Initialize `max_reach = 0`.
2. Traverse the array.
3. If current index > max_reach → return False.
4. Update `max_reach`.
5. Return True.

### Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

---

### 2. Check Equal Arrays

### Problem Statement

Determine whether two arrays contain the same elements with the same frequency.

### Approach

- Count the frequency of elements in the first array.
- Reduce the frequency using the second array.
- If every frequency becomes zero, the arrays are equal.

### Algorithm

1. Check array lengths.
2. Create a frequency dictionary.
3. Count occurrences in the first array.
4. Decrease counts using the second array.
5. Return True if all frequencies match.

### Complexity

- Time Complexity: O(n)
- Space Complexity: O(n)

---

# 🧠 Concepts Learned

- Greedy Algorithm
- Maximum Reach
- Array Traversal
- Hash Map (Dictionary)
- Frequency Counting
- Decision Making

---

# 📚 Interview Questions

### Jump Game

- Why is Greedy better than checking every possible jump?
- What does `max_reach` represent?
- Can this be solved using Dynamic Programming?

### Check Equal Arrays

- Why use a dictionary?
- Can sorting also solve this problem?
- Which approach is more efficient?

---

## ✅ Status

✔ Problem 1 Completed

✔ Problem 2 Completed

**Language Used:** Python 🐍
# 📅 Day 012

## Problems Solved

### 1. Number of Lines To Write String (LeetCode #806)

### Problem Statement

Given the width of every lowercase letter and a string, determine:

- Total number of lines required.
- Width occupied by the last line.

Each line can contain at most **100 units**.

### Approach

- Traverse each character.
- Calculate its width.
- If adding the character exceeds 100 units, move to the next line.
- Otherwise, continue writing on the current line.

### Algorithm

1. Initialize one line.
2. Traverse the string.
3. Get each character's width.
4. Check whether it fits on the current line.
5. Update line count and width.

### Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

---

### 2. Smallest Distinct Window

### Problem Statement

Find the length of the smallest substring containing every distinct character of the given string.

### Approach

- Count the total distinct characters.
- Use the Sliding Window technique.
- Expand the window until all distinct characters are included.
- Shrink the window while maintaining validity.

### Algorithm

1. Count distinct characters.
2. Expand the right pointer.
3. Maintain character frequencies.
4. Shrink the left pointer whenever possible.
5. Store the minimum window length.

### Complexity

- Time Complexity: O(n)
- Space Complexity: O(n)

---

# 🧠 Concepts Learned

- Simulation
- Character Width Mapping
- Sliding Window
- Hash Map (Dictionary)
- Frequency Counting
- Two Pointer Technique

---

# 📚 Interview Questions

### Number of Lines

- Why use `ord()`?
- Why is the maximum line width 100?
- What happens if a character doesn't fit on the current line?

### Smallest Distinct Window

- What is Sliding Window?
- Why use a frequency dictionary?
- Can this problem be solved using brute force?

---

## ✅ Status

✔ Problem 1 Completed

✔ Problem 2 Completed

**Language Used:** Python 🐍
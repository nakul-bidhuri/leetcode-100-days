# 📅 Day 009

## Problems Solved

### 1. Length of Last Word (LeetCode #58)

### Problem Statement

Given a string containing words and spaces, return the length of the last word.

### Approach

- Remove leading and trailing spaces.
- Traverse the string from the end.
- Count characters until a space is found.

### Algorithm

1. Remove extra spaces using `strip()`.
2. Start from the last character.
3. Count characters until a space appears.
4. Return the count.

### Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

---

### 2. Remove Spaces from String

### Problem Statement

Remove all spaces from the given string.

### Approach

- Traverse each character.
- Skip spaces.
- Append non-space characters to a new string.

### Algorithm

1. Create an empty string.
2. Traverse every character.
3. Ignore spaces.
4. Append remaining characters.
5. Return the final string.

### Complexity

- Time Complexity: O(n)
- Space Complexity: O(n)

---

# 🧠 Concepts Learned

- String Traversal
- Whitespace Handling
- Character Filtering
- Reverse Traversal
- String Building

---

# 📚 Interview Questions

### Length of Last Word

- Why do we use `strip()`?
- Why traverse from the end?
- Can this be solved using `split()`?

### Remove Spaces

- Why create a new string?
- Can this be done in-place?
- What's the difference between removing all spaces and trimming spaces?

---

## ✅ Status

✔ Problem 1 Completed

✔ Problem 2 Completed

**Language Used:** Python 🐍
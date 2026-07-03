# 📅 Day 010

## Problems Solved

### 1. Find the Index of the First Occurrence in a String (LeetCode #28)

### Problem Statement

Given two strings `haystack` and `needle`, return the index of the first occurrence of `needle` in `haystack`. If it is not found, return `-1`.

### Approach

- Traverse the main string.
- Compare every possible substring with the target string.
- Return the first matching index.
- Return `-1` if no match is found.

### Algorithm

1. Calculate lengths of both strings.
2. Traverse from index `0` to `n-m`.
3. Compare substring with `needle`.
4. Return index if matched.
5. Otherwise return `-1`.

### Complexity

- Time Complexity: O(n × m)
- Space Complexity: O(1)

---

### 2. Determine Gender

### Problem Statement

Determine the output based on the number of distinct characters in the username.

- Even distinct characters → **CHAT WITH HER!**
- Odd distinct characters → **IGNORE HIM!**

### Approach

- Store all unique characters.
- Count them.
- Check if the count is even or odd.

### Algorithm

1. Create a set of characters.
2. Count distinct characters.
3. Check parity.
4. Print the corresponding message.

### Complexity

- Time Complexity: O(n)
- Space Complexity: O(n)

---

# 🧠 Concepts Learned

- String Searching
- Substring Matching
- String Traversal
- Sets
- Distinct Characters
- Even/Odd Logic

---

# 📚 Interview Questions

### First Occurrence

- Why compare substrings?
- Can this be solved faster than O(n × m)?
- What is the KMP Algorithm?

### Determine Gender

- Why use a set?
- How does a set remove duplicates?
- Can this be solved without using a set?

---

## ✅ Status

✔ Problem 1 Completed

✔ Problem 2 Completed

**Language Used:** Python 🐍
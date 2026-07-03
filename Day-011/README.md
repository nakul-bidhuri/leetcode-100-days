# 📅 Day 011

## Problems Solved

### 1. Isomorphic Strings (LeetCode #205)

### Problem Statement

Given two strings `s` and `t`, determine whether they are isomorphic.

Two strings are isomorphic if every character in one string maps to exactly one character in the other string while preserving the order.

### Approach

- Use two dictionaries.
- Store character mappings in both directions.
- If any mapping conflicts, return False.

### Algorithm

1. Check lengths.
2. Create two dictionaries.
3. Traverse both strings.
4. Verify mappings.
5. Return True if no conflicts are found.

### Complexity

- Time Complexity: O(n)
- Space Complexity: O(n)

---

### 2. String Processing Task

### Problem Statement

Given a string:

- Remove all vowels.
- Convert uppercase consonants to lowercase.
- Add '.' before every consonant.

### Approach

- Traverse every character.
- Skip vowels.
- Convert consonants to lowercase.
- Append '.' before every consonant.

### Algorithm

1. Store all vowels.
2. Traverse the string.
3. Skip vowels.
4. Append "." + lowercase character.
5. Return the final string.

### Complexity

- Time Complexity: O(n)
- Space Complexity: O(n)

---

# 🧠 Concepts Learned

- Hash Maps (Dictionary)
- Character Mapping
- String Traversal
- Character Filtering
- Case Conversion
- Pattern Recognition

---

# 📚 Interview Questions

### Isomorphic Strings

- Why are two dictionaries needed?
- What happens if two characters map to the same character?
- Can this be solved using arrays?

### String Processing

- Why use `lower()`?
- Why remove vowels first?
- How do we identify vowels efficiently?

---

## ✅ Status

✔ Problem 1 Completed

✔ Problem 2 Completed

**Language Used:** Python 🐍
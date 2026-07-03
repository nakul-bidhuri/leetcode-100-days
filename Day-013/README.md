# 📅 Day 013

## Problems Solved

### 1. Most Common Word (LeetCode #819)

### Problem Statement

Given a paragraph and a list of banned words, return the most common word that is not banned.

Ignore punctuation and uppercase/lowercase differences.

### Approach

- Convert everything to lowercase.
- Extract only words.
- Store banned words in a set.
- Count word frequencies using a dictionary.
- Return the word with the highest frequency.

### Algorithm

1. Convert paragraph to lowercase.
2. Remove punctuation.
3. Traverse every word.
4. Skip banned words.
5. Count frequencies.
6. Return the most frequent word.

### Complexity

- Time Complexity: O(n)
- Space Complexity: O(n)

---

### 2. Better String

### Problem Statement

Given two strings, return the one having more distinct subsequences.

If both have the same number, return the first string.

### Approach

- Use Dynamic Programming.
- Track the last occurrence of each character.
- Count distinct subsequences efficiently.

### Algorithm

1. Create a DP array.
2. Double previous count.
3. Remove duplicate subsequences using the last occurrence.
4. Compare both strings.
5. Return the better string.

### Complexity

- Time Complexity: O(n)
- Space Complexity: O(n)

---

# 🧠 Concepts Learned

- Regular Expressions
- Hash Map (Dictionary)
- Sets
- Frequency Counting
- Dynamic Programming
- Distinct Subsequences

---

# 📚 Interview Questions

### Most Common Word

- Why use Regular Expressions?
- Why convert to lowercase?
- Why use a set for banned words?

### Better String

- What is a subsequence?
- Why is Dynamic Programming needed?
- Why track the last occurrence?

---

## ✅ Status

✔ Problem 1 Completed

✔ Problem 2 Completed

**Language Used:** Python 🐍
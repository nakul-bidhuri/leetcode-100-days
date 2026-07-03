# 📅 Day 019

## Problems Solved

### 1. Remove Duplicates from Sorted List (LeetCode #83)

### Problem Statement

Given the head of a sorted linked list, remove duplicate nodes so that every value appears only once.

### Approach

- Since the linked list is sorted, duplicate values will always be next to each other.
- Traverse the list using a pointer.
- If current node value equals next node value, skip the next node.
- Otherwise, move forward.

### Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

---

### 2. Middle of the Linked List

### Problem Statement

Given the head of a linked list, return the middle node.

If there are two middle nodes, return the second middle node.

### Approach

- Use slow and fast pointers.
- Slow moves one step.
- Fast moves two steps.
- When fast reaches the end, slow will be at the middle.

### Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

---

# 🧠 Concepts Learned

- Linked List Traversal
- In-place Node Removal
- Fast and Slow Pointer
- Single Pass Algorithm
- Sorted Linked List Handling

---

# 📚 Interview Questions

### Remove Duplicates

- Why does this work only easily on a sorted linked list?
- Why do we use `current.next = current.next.next`?
- What happens if duplicates appear more than twice?

### Middle of Linked List

- Why does the slow pointer reach the middle?
- Why does fast move two steps?
- What happens when the list has even length?

---

## ✅ Status

✔ Problem 1 Completed

✔ Problem 2 Completed

**Language Used:** Python 🐍
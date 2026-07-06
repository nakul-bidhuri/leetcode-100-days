# 📅 Day 020

## Problems Solved

### 1. Remove Linked List Elements (LeetCode #203)

### Problem Statement

Given the head of a linked list and an integer value, remove every node whose value equals the given value.

### Approach

- Create a dummy node.
- Traverse the linked list.
- Skip every node whose value equals the target.
- Return the new head.

### Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

---

### 2. Segregate Even and Odd Nodes

### Problem Statement

Rearrange a linked list so that all even-valued nodes appear before all odd-valued nodes while maintaining their original relative order.

### Approach

- Create two temporary linked lists:
  - Even list
  - Odd list
- Traverse the original list.
- Append each node to the correct list.
- Join the even list with the odd list.

### Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

---

# 🧠 Concepts Learned

- Linked List Traversal
- In-place Node Deletion
- Dummy Node
- Pointer Manipulation
- Even/Odd Segregation

---

# 📚 Interview Questions

### Remove Linked List Elements

- Why is a dummy node useful?
- Why don't we move the pointer after deleting a node?
- What happens if the first node must be deleted?

### Segregate Even and Odd Nodes

- Why create separate even and odd lists?
- How is the original order preserved?
- Can this be done without creating new nodes?

---

## ✅ Status

✔ Problem 1 Completed

✔ Problem 2 Completed

**Language Used:** Python 🐍
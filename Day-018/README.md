# 📅 Day 018

# Problems Solved

## 1. Rotate List (LeetCode #61)

### Problem Statement

Given the head of a linked list, rotate the list to the right by **k** places.

### Example

**Input**

```
1 → 2 → 3 → 4 → 5
k = 2
```

**Output**

```
4 → 5 → 1 → 2 → 3
```

### Approach

- Find the length of the linked list.
- Connect the last node to the head to form a circular linked list.
- Calculate the effective rotation using `k % length`.
- Find the new tail.
- Break the circle to get the rotated list.

### Algorithm

1. Find the length of the linked list.
2. Connect the last node to the head.
3. Compute `k = k % length`.
4. Move to the new tail.
5. Break the circular link.
6. Return the new head.

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

## 2. Remove Nth Node From End of Linked List

### Problem Statement

Given the head of a linked list, remove the **nth** node from the end and return the updated linked list.

### Example

**Input**

```
1 → 2 → 3 → 4 → 5
n = 2
```

**Output**

```
1 → 2 → 3 → 5
```

### Approach

- Create a dummy node.
- Use two pointers (`fast` and `slow`).
- Move the `fast` pointer `n + 1` steps ahead.
- Move both pointers together until `fast` reaches the end.
- Delete the required node.

### Algorithm

1. Create a dummy node.
2. Move the fast pointer `n + 1` steps.
3. Move both pointers together.
4. Delete `slow.next`.
5. Return `dummy.next`.

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

# 🧠 Concepts Learned

- Linked List Rotation
- Circular Linked List
- Dummy Node
- Fast & Slow Pointer Technique
- Two Pointer Technique
- Linked List Deletion

---

# 📚 Interview Questions

## Rotate List

- Why do we calculate `k % length`?
- Why do we temporarily make the list circular?
- What happens if `k` is equal to the length of the list?

## Remove Nth Node

- Why is a dummy node useful?
- Why move the fast pointer `n + 1` steps?
- Can this be solved in one traversal?

---

# ❌ Common Mistakes

### Rotate List

- Forgetting to calculate `k % length`.
- Not breaking the circular linked list.
- Forgetting the cases where the list is empty or has one node.

### Remove Nth Node

- Forgetting to use a dummy node.
- Moving the fast pointer the wrong number of steps.
- Not handling deletion of the first node correctly.

---

# 💡 Real Interview Tip

Both of these are **Top 100 Linked List interview questions**.

Interviewers expect you to:

- Understand pointer movement.
- Draw the linked list on paper.
- Explain every pointer update clearly.
- Handle edge cases like:
  - Empty list
  - Single node
  - `k = 0`
  - `k > length`
  - Removing the first node

---

# 📚 Revision

Today you learned:

- ✅ Circular Linked Lists
- ✅ Rotating Linked Lists
- ✅ Two Pointer Technique
- ✅ Dummy Nodes
- ✅ Single Pass Algorithms
- ✅ Linked List Deletion

---

# 🎯 Practice Challenge

### Challenge 1

Rotate:

```
10 → 20 → 30 → 40
k = 1
```

Expected Output

```
40 → 10 → 20 → 30
```

---

### Challenge 2

Remove the 3rd node from the end:

```
5 → 6 → 7 → 8 → 9
```

Expected Output

```
5 → 6 → 8 → 9
```

---

## ✅ Status

- ✔ Problem 1 Completed
- ✔ Problem 2 Completed

**Language Used:** Python 🐍